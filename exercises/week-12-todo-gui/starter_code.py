#!/usr/bin/env python3
"""
Todo GUI Application - Starter Code
Week 12 Project

TODO: Create a complete todo list application with GUI
"""

import tkinter as tk
from tkinter import ttk, messagebox
import json
from datetime import datetime

class Task:
    """Represents a single task"""
    
    def __init__(self, description, priority="Medium"):
        # TODO: Initialize task properties
        # TODO: Generate unique ID
        # TODO: Set creation timestamp
        # TODO: Set completion status to False
        pass
    
    def to_dict(self):
        """Convert task to dictionary for saving"""
        # TODO: Return dictionary with all task data
        return {}
    
    @classmethod
    def from_dict(cls, data):
        """Create task from dictionary"""
        # TODO: Create task instance from saved data
        # TODO: Handle missing fields gracefully
        pass

class TaskManager:
    """Manages the list of tasks"""
    
    def __init__(self, filename="todo_data.json"):
        self.filename = filename
        self.tasks = []
        self.load_tasks()
    
    def add_task(self, description, priority="Medium"):
        """Add a new task"""
        # TODO: Create new Task instance
        # TODO: Add to tasks list
        # TODO: Save tasks to file
        pass
    
    def complete_task(self, task_id):
        """Mark a task as completed"""
        # TODO: Find task by ID
        # TODO: Set completed to True
        # TODO: Save tasks to file
        pass
    
    def delete_task(self, task_id):
        """Delete a task"""
        # TODO: Find and remove task by ID
        # TODO: Save tasks to file
        pass
    
    def get_active_tasks(self):
        """Get list of incomplete tasks"""
        # TODO: Return list of tasks where completed is False
        return []
    
    def get_completed_tasks(self):
        """Get list of completed tasks"""
        # TODO: Return list of tasks where completed is True
        return []
    
    def clear_completed(self):
        """Remove all completed tasks"""
        # TODO: Filter out completed tasks
        # TODO: Save tasks to file
        pass
    
    def save_tasks(self):
        """Save tasks to JSON file"""
        # TODO: Convert tasks to dictionaries
        # TODO: Write to JSON file
        # TODO: Handle file errors
        pass
    
    def load_tasks(self):
        """Load tasks from JSON file"""
        # TODO: Try to read JSON file
        # TODO: Convert dictionaries to Task objects
        # TODO: Handle file not found
        pass

class TodoApp:
    """Main GUI application"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("✅ My Todo List")
        self.root.geometry("500x400")
        
        # Initialize task manager
        self.task_manager = TaskManager()
        
        # Create GUI elements
        self.create_widgets()
        self.refresh_task_list()
        
        # Bind keyboard shortcuts
        self.bind_shortcuts()
    
    def create_widgets(self):
        """Create and layout GUI widgets"""
        # TODO: Create main frame
        # TODO: Create title label
        # TODO: Create input frame (entry + button)
        # TODO: Create task list frame
        # TODO: Create button frame
        # TODO: Create status bar
        # TODO: Layout all widgets
        pass
    
    def add_task(self):
        """Add a new task from input field"""
        # TODO: Get text from entry widget
        # TODO: Validate input (not empty)
        # TODO: Add task using task manager
        # TODO: Clear input field
        # TODO: Refresh task list
        # TODO: Update status
        pass
    
    def on_task_toggle(self, task_id):
        """Handle task completion toggle"""
        # TODO: Toggle task completion status
        # TODO: Refresh task list
        # TODO: Update status
        pass
    
    def delete_task(self, task_id):
        """Delete a specific task"""
        # TODO: Confirm deletion with user
        # TODO: Delete task using task manager
        # TODO: Refresh task list
        # TODO: Update status
        pass
    
    def clear_completed_tasks(self):
        """Clear all completed tasks"""
        # TODO: Confirm action with user
        # TODO: Clear completed tasks
        # TODO: Refresh task list
        # TODO: Update status
        pass
    
    def refresh_task_list(self):
        """Update the task list display"""
        # TODO: Clear current task list widget
        # TODO: Get all tasks from task manager
        # TODO: Create widgets for each task
        # TODO: Add checkboxes and delete buttons
        # TODO: Handle task state (completed/active)
        pass
    
    def update_status(self):
        """Update status bar with task counts"""
        # TODO: Count active and completed tasks
        # TODO: Update status label text
        pass
    
    def bind_shortcuts(self):
        """Bind keyboard shortcuts"""
        # TODO: Bind Enter key to add task
        # TODO: Bind Ctrl+S to save
        # TODO: Bind Delete key for selected tasks
        pass
    
    def on_enter_pressed(self, event):
        """Handle Enter key press"""
        # TODO: Add task when Enter is pressed in input field
        pass

def main():
    """Main program"""
    # Create and run the application
    root = tk.Tk()
    app = TodoApp(root)
    
    try:
        root.mainloop()
    except KeyboardInterrupt:
        print("\nApplication closed")

if __name__ == "__main__":
    main()

