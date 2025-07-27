#!/usr/bin/env python3
"""
Todo GUI Application - Complete Solution
Week 12 Project

This solution implements a complete todo list application with GUI,
task persistence, and priority management.
"""

import tkinter as tk
from tkinter import ttk, messagebox
import json
from datetime import datetime
import uuid
import os

class Task:
    """Represents a single task"""
    
    def __init__(self, description, priority="Medium"):
        self.id = str(uuid.uuid4())
        self.description = description
        self.priority = priority
        self.completed = False
        self.created_at = datetime.now().isoformat()
        self.completed_at = None
    
    def to_dict(self):
        """Convert task to dictionary for saving"""
        return {
            "id": self.id,
            "description": self.description,
            "priority": self.priority,
            "completed": self.completed,
            "created_at": self.created_at,
            "completed_at": self.completed_at
        }
    
    @classmethod
    def from_dict(cls, data):
        """Create task from dictionary"""
        task = cls(data.get("description", ""), data.get("priority", "Medium"))
        task.id = data.get("id", str(uuid.uuid4()))
        task.completed = data.get("completed", False)
        task.created_at = data.get("created_at", datetime.now().isoformat())
        task.completed_at = data.get("completed_at", None)
        return task

class TaskManager:
    """Manages the list of tasks"""
    
    def __init__(self, filename="todo_data.json"):
        self.filename = filename
        self.tasks = []
        self.load_tasks()
    
    def add_task(self, description, priority="Medium"):
        """Add a new task"""
        task = Task(description, priority)
        self.tasks.append(task)
        self.save_tasks()
        return task
    
    def complete_task(self, task_id):
        """Mark a task as completed"""
        for task in self.tasks:
            if task.id == task_id:
                task.completed = True
                task.completed_at = datetime.now().isoformat()
                self.save_tasks()
                return True
        return False
    
    def uncomplete_task(self, task_id):
        """Mark a task as not completed"""
        for task in self.tasks:
            if task.id == task_id:
                task.completed = False
                task.completed_at = None
                self.save_tasks()
                return True
        return False
    
    def delete_task(self, task_id):
        """Delete a task"""
        self.tasks = [t for t in self.tasks if t.id != task_id]
        self.save_tasks()
    
    def update_task(self, task_id, description=None, priority=None):
        """Update task properties"""
        for task in self.tasks:
            if task.id == task_id:
                if description:
                    task.description = description
                if priority:
                    task.priority = priority
                self.save_tasks()
                return True
        return False
    
    def get_active_tasks(self):
        """Get list of incomplete tasks"""
        return [t for t in self.tasks if not t.completed]
    
    def get_completed_tasks(self):
        """Get list of completed tasks"""
        return [t for t in self.tasks if t.completed]
    
    def clear_completed(self):
        """Remove all completed tasks"""
        self.tasks = [t for t in self.tasks if not t.completed]
        self.save_tasks()
    
    def save_tasks(self):
        """Save tasks to JSON file"""
        try:
            task_data = [task.to_dict() for task in self.tasks]
            with open(self.filename, 'w') as f:
                json.dump(task_data, f, indent=2)
        except Exception as e:
            print(f"Error saving tasks: {e}")
    
    def load_tasks(self):
        """Load tasks from JSON file"""
        try:
            with open(self.filename, 'r') as f:
                task_data = json.load(f)
            self.tasks = [Task.from_dict(data) for data in task_data]
        except FileNotFoundError:
            self.tasks = []  # Start with empty list
        except Exception as e:
            print(f"Error loading tasks: {e}")
            self.tasks = []

class TodoApp:
    """Main GUI application"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("✅ My Todo List")
        self.root.geometry("600x500")
        
        # Configure style
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Initialize task manager
        self.task_manager = TaskManager()
        
        # Track task widgets for updates
        self.task_widgets = {}
        
        # Filter state
        self.filter_var = tk.StringVar(value="all")
        
        # Create GUI elements
        self.create_widgets()
        self.refresh_task_list()
        
        # Bind keyboard shortcuts
        self.bind_shortcuts()
    
    def create_widgets(self):
        """Create and layout GUI widgets"""
        # Main container
        main_container = ttk.Frame(self.root, padding="10")
        main_container.pack(fill="both", expand=True)
        
        # Title
        title_label = tk.Label(main_container, text="✅ My Todo List", 
                              font=("Arial", 20, "bold"), fg="#2c3e50")
        title_label.pack(pady=(0, 10))
        
        # Input frame
        input_frame = ttk.Frame(main_container)
        input_frame.pack(fill="x", pady=(0, 10))
        
        # Task entry
        self.task_var = tk.StringVar()
        self.task_entry = ttk.Entry(input_frame, textvariable=self.task_var, 
                                   width=35, font=("Arial", 11))
        self.task_entry.pack(side="left", padx=(0, 5))
        
        # Priority dropdown
        self.priority_var = tk.StringVar(value="Medium")
        priority_combo = ttk.Combobox(input_frame, textvariable=self.priority_var,
                                     values=["Low", "Medium", "High"], 
                                     width=10, state="readonly")
        priority_combo.pack(side="left", padx=(0, 5))
        
        # Add button
        add_btn = ttk.Button(input_frame, text="Add Task", 
                            command=self.add_task)
        add_btn.pack(side="left")
        
        # Filter frame
        filter_frame = ttk.Frame(main_container)
        filter_frame.pack(fill="x", pady=(0, 10))
        
        ttk.Label(filter_frame, text="Show:").pack(side="left", padx=(0, 5))
        
        filters = [("All", "all"), ("Active", "active"), ("Completed", "completed")]
        for text, value in filters:
            ttk.Radiobutton(filter_frame, text=text, variable=self.filter_var,
                           value=value, command=self.refresh_task_list).pack(side="left", padx=5)
        
        # Task list frame with scrollbar
        list_container = ttk.Frame(main_container)
        list_container.pack(fill="both", expand=True, pady=(0, 10))
        
        # Canvas and scrollbar for task list
        self.canvas = tk.Canvas(list_container, bg="white", highlightthickness=1,
                               highlightbackground="#ddd")
        scrollbar = ttk.Scrollbar(list_container, orient="vertical", 
                                 command=self.canvas.yview)
        self.scrollable_frame = ttk.Frame(self.canvas)
        
        self.canvas.configure(yscrollcommand=scrollbar.set)
        self.canvas_window = self.canvas.create_window((0, 0), 
                                                       window=self.scrollable_frame, 
                                                       anchor="nw")
        
        self.canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Bind canvas events
        self.scrollable_frame.bind("<Configure>", 
                                  lambda e: self.canvas.configure(
                                      scrollregion=self.canvas.bbox("all")))
        
        # Enable mouse wheel scrolling
        self.canvas.bind_all("<MouseWheel>", self.on_mousewheel)  # Windows
        self.canvas.bind_all("<Button-4>", 
                            lambda e: self.canvas.yview_scroll(-1, "units"))  # Linux
        self.canvas.bind_all("<Button-5>", 
                            lambda e: self.canvas.yview_scroll(1, "units"))   # Linux
        
        # Button frame
        button_frame = ttk.Frame(main_container)
        button_frame.pack(fill="x", pady=(0, 5))
        
        clear_btn = ttk.Button(button_frame, text="Clear Completed", 
                              command=self.clear_completed_tasks)
        clear_btn.pack(side="left", padx=(0, 5))
        
        # Statistics frame
        stats_frame = ttk.Frame(button_frame)
        stats_frame.pack(side="right")
        
        self.stats_label = ttk.Label(stats_frame, text="", font=("Arial", 9))
        self.stats_label.pack()
        
        # Status bar
        self.status_var = tk.StringVar()
        status_bar = ttk.Label(self.root, textvariable=self.status_var, 
                              relief="sunken", anchor="w")
        status_bar.pack(side="bottom", fill="x")
        
        self.update_status()
    
    def on_mousewheel(self, event):
        """Handle mouse wheel scrolling"""
        self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")
    
    def add_task(self):
        """Add a new task from input field"""
        description = self.task_var.get().strip()
        
        if not description:
            messagebox.showwarning("Empty Task", 
                                 "Please enter a task description!")
            self.task_entry.focus()
            return
        
        priority = self.priority_var.get()
        task = self.task_manager.add_task(description, priority)
        
        # Clear input and reset priority
        self.task_var.set("")
        self.priority_var.set("Medium")
        self.task_entry.focus()
        
        # Refresh display
        self.refresh_task_list()
        
        # Show confirmation
        self.status_var.set(f"Added task: {description}")
    
    def on_task_toggle(self, task_id):
        """Handle task completion toggle"""
        task = next((t for t in self.task_manager.tasks if t.id == task_id), None)
        if task:
            if task.completed:
                self.task_manager.uncomplete_task(task_id)
            else:
                self.task_manager.complete_task(task_id)
            self.refresh_task_list()
    
    def delete_task(self, task_id):
        """Delete a specific task"""
        task = next((t for t in self.task_manager.tasks if t.id == task_id), None)
        if task:
            result = messagebox.askyesno("Delete Task", 
                                       f"Delete '{task.description}'?")
            if result:
                self.task_manager.delete_task(task_id)
                self.refresh_task_list()
                self.status_var.set(f"Deleted task: {task.description}")
    
    def edit_task(self, task_id):
        """Edit a task description"""
        task = next((t for t in self.task_manager.tasks if t.id == task_id), None)
        if not task:
            return
        
        # Create edit dialog
        dialog = tk.Toplevel(self.root)
        dialog.title("Edit Task")
        dialog.geometry("400x150")
        dialog.transient(self.root)
        dialog.grab_set()
        
        # Center the dialog
        dialog.update_idletasks()
        x = (dialog.winfo_screenwidth() // 2) - (dialog.winfo_width() // 2)
        y = (dialog.winfo_screenheight() // 2) - (dialog.winfo_height() // 2)
        dialog.geometry(f"+{x}+{y}")
        
        # Dialog content
        ttk.Label(dialog, text="Task Description:").pack(pady=5)
        
        desc_var = tk.StringVar(value=task.description)
        desc_entry = ttk.Entry(dialog, textvariable=desc_var, width=40)
        desc_entry.pack(pady=5, padx=20, fill="x")
        desc_entry.select_range(0, tk.END)
        desc_entry.focus()
        
        # Priority selection
        priority_frame = ttk.Frame(dialog)
        priority_frame.pack(pady=5)
        
        ttk.Label(priority_frame, text="Priority:").pack(side="left", padx=5)
        priority_var = tk.StringVar(value=task.priority)
        priority_combo = ttk.Combobox(priority_frame, textvariable=priority_var,
                                     values=["Low", "Medium", "High"], 
                                     width=10, state="readonly")
        priority_combo.pack(side="left")
        
        # Buttons
        button_frame = ttk.Frame(dialog)
        button_frame.pack(pady=10)
        
        def save_changes():
            new_desc = desc_var.get().strip()
            if new_desc:
                self.task_manager.update_task(task_id, new_desc, priority_var.get())
                self.refresh_task_list()
                self.status_var.set(f"Updated task: {new_desc}")
                dialog.destroy()
            else:
                messagebox.showwarning("Empty Task", 
                                     "Task description cannot be empty!")
        
        ttk.Button(button_frame, text="Save", 
                  command=save_changes).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Cancel", 
                  command=dialog.destroy).pack(side="left")
        
        # Bind Enter key
        desc_entry.bind('<Return>', lambda e: save_changes())
    
    def clear_completed_tasks(self):
        """Clear all completed tasks"""
        completed_count = len(self.task_manager.get_completed_tasks())
        
        if completed_count == 0:
            messagebox.showinfo("No Completed Tasks", 
                              "There are no completed tasks to clear.")
            return
        
        result = messagebox.askyesno("Clear Completed", 
                                   f"Remove {completed_count} completed task(s)?")
        if result:
            self.task_manager.clear_completed()
            self.refresh_task_list()
            self.status_var.set(f"Cleared {completed_count} completed task(s)")
    
    def refresh_task_list(self):
        """Update the task list display"""
        # Clear existing widgets
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()
        self.task_widgets.clear()
        
        # Get tasks based on filter
        filter_value = self.filter_var.get()
        if filter_value == "active":
            tasks = self.task_manager.get_active_tasks()
        elif filter_value == "completed":
            tasks = self.task_manager.get_completed_tasks()
        else:
            tasks = self.task_manager.tasks
        
        # Sort tasks: uncompleted first, then by priority
        priority_order = {"High": 0, "Medium": 1, "Low": 2}
        tasks.sort(key=lambda t: (t.completed, priority_order.get(t.priority, 3)))
        
        # Display each task
        for i, task in enumerate(tasks):
            self.create_task_widget(task, i)
        
        # Show empty message if no tasks
        if not tasks:
            empty_msg = "No tasks yet. Add one above!" if filter_value == "all" else f"No {filter_value} tasks."
            empty_label = ttk.Label(self.scrollable_frame, text=empty_msg,
                                   font=("Arial", 11), foreground="#999")
            empty_label.pack(pady=50)
        
        self.update_status()
        self.update_statistics()
    
    def create_task_widget(self, task, index):
        """Create widget for a single task"""
        # Task frame
        task_frame = ttk.Frame(self.scrollable_frame)
        task_frame.pack(fill="x", padx=10, pady=3)
        
        # Alternate background colors
        if index % 2 == 0:
            task_frame.configure(style="Even.TFrame")
        
        # Checkbox
        var = tk.BooleanVar(value=task.completed)
        check = ttk.Checkbutton(task_frame, variable=var,
                               command=lambda: self.on_task_toggle(task.id))
        check.pack(side="left", padx=(5, 10))
        
        # Task description
        desc_frame = ttk.Frame(task_frame)
        desc_frame.pack(side="left", fill="x", expand=True)
        
        # Task text
        font_style = ("Arial", 10, "overstrike") if task.completed else ("Arial", 10)
        text_color = "#999" if task.completed else "#333"
        
        desc_label = tk.Label(desc_frame, text=task.description, 
                             font=font_style, fg=text_color, bg="white",
                             anchor="w", justify="left")
        desc_label.pack(anchor="w")
        
        # Task metadata (priority and time)
        meta_text = f"{task.priority} priority"
        if task.completed and task.completed_at:
            completed_time = datetime.fromisoformat(task.completed_at)
            meta_text += f" • Completed {completed_time.strftime('%b %d at %I:%M %p')}"
        else:
            created_time = datetime.fromisoformat(task.created_at)
            # Show relative time
            time_diff = datetime.now() - created_time
            if time_diff.days > 0:
                meta_text += f" • {time_diff.days} day(s) ago"
            elif time_diff.seconds > 3600:
                hours = time_diff.seconds // 3600
                meta_text += f" • {hours} hour(s) ago"
            else:
                minutes = time_diff.seconds // 60
                meta_text += f" • {minutes} minute(s) ago"
        
        meta_label = tk.Label(desc_frame, text=meta_text,
                             font=("Arial", 8), fg="#666", bg="white")
        meta_label.pack(anchor="w")
        
        # Priority indicator
        priority_colors = {
            "Low": "#4CAF50",    # Green
            "Medium": "#FF9800",  # Orange  
            "High": "#F44336"     # Red
        }
        
        priority_indicator = tk.Frame(task_frame, width=4, 
                                    bg=priority_colors.get(task.priority, "#999"))
        priority_indicator.pack(side="left", fill="y", padx=(0, 10))
        
        # Action buttons
        button_frame = ttk.Frame(task_frame)
        button_frame.pack(side="right", padx=5)
        
        # Edit button (only for uncompleted tasks)
        if not task.completed:
            edit_btn = ttk.Button(button_frame, text="✏️", width=3,
                                 command=lambda: self.edit_task(task.id))
            edit_btn.pack(side="left", padx=2)
        
        # Delete button
        delete_btn = ttk.Button(button_frame, text="🗑️", width=3,
                               command=lambda: self.delete_task(task.id))
        delete_btn.pack(side="left", padx=2)
        
        # Store widget reference
        self.task_widgets[task.id] = task_frame
    
    def update_status(self):
        """Update status bar with task counts"""
        active = len(self.task_manager.get_active_tasks())
        completed = len(self.task_manager.get_completed_tasks())
        total = len(self.task_manager.tasks)
        
        if total == 0:
            self.status_var.set("Ready to add tasks")
        else:
            self.status_var.set(f"Tasks: {active} active, {completed} completed, {total} total")
    
    def update_statistics(self):
        """Update statistics display"""
        active_tasks = self.task_manager.get_active_tasks()
        
        # Count by priority
        priority_counts = {"High": 0, "Medium": 0, "Low": 0}
        for task in active_tasks:
            priority_counts[task.priority] += 1
        
        # Build statistics text
        if any(priority_counts.values()):
            stats_parts = []
            if priority_counts["High"] > 0:
                stats_parts.append(f"🔴 {priority_counts['High']}")
            if priority_counts["Medium"] > 0:
                stats_parts.append(f"🟡 {priority_counts['Medium']}")
            if priority_counts["Low"] > 0:
                stats_parts.append(f"🟢 {priority_counts['Low']}")
            
            self.stats_label.config(text=" | ".join(stats_parts))
        else:
            self.stats_label.config(text="")
    
    def bind_shortcuts(self):
        """Bind keyboard shortcuts"""
        # Enter key to add task
        self.task_entry.bind('<Return>', self.on_enter_pressed)
        
        # Ctrl+S to save (though we auto-save)
        self.root.bind('<Control-s>', lambda e: self.task_manager.save_tasks())
        
        # Escape to clear input
        self.root.bind('<Escape>', lambda e: self.task_var.set(""))
        
        # Ctrl+D to clear completed
        self.root.bind('<Control-d>', lambda e: self.clear_completed_tasks())
        
        # Set focus to entry on startup
        self.task_entry.focus()
    
    def on_enter_pressed(self, event):
        """Handle Enter key press"""
        self.add_task()

def main():
    """Main program"""
    # Create and run the application
    root = tk.Tk()
    
    # Set icon if available
    try:
        root.iconbitmap('icon.ico')
    except:
        pass
    
    app = TodoApp(root)
    
    # Center window on screen
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f"{width}x{height}+{x}+{y}")
    
    try:
        root.mainloop()
    except KeyboardInterrupt:
        print("\nApplication closed")

if __name__ == "__main__":
    main()