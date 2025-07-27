# Todo GUI Application - Hints 💡

## Stuck? Here are some hints to help you progress!

### General Structure Hints

**Hint 1: Task Class Structure**
```python
class Task:
    def __init__(self, description, priority="Medium"):
        self.id = str(uuid.uuid4())  # Or use timestamp
        self.description = description
        self.priority = priority
        self.completed = False
        self.created_at = datetime.now().isoformat()
```

**Hint 2: Basic GUI Layout**
```python
# Main window structure
root = tk.Tk()
root.title("✅ My Todo List")
root.geometry("500x400")

# Frame hierarchy
main_frame = ttk.Frame(root, padding="10")
input_frame = ttk.Frame(main_frame)
list_frame = ttk.Frame(main_frame)
button_frame = ttk.Frame(main_frame)
```

### Class Implementation Hints

**Task Class - to_dict() Hints:**
```python
def to_dict(self):
    return {
        "id": self.id,
        "description": self.description,
        "priority": self.priority,
        "completed": self.completed,
        "created_at": self.created_at
    }
```

**Task Class - from_dict() Hints:**
```python
@classmethod
def from_dict(cls, data):
    task = cls(data.get("description", ""), data.get("priority", "Medium"))
    task.id = data.get("id", str(uuid.uuid4()))
    task.completed = data.get("completed", False)
    task.created_at = data.get("created_at", datetime.now().isoformat())
    return task
```

### TaskManager Implementation

**add_task() Hints:**
```python
def add_task(self, description, priority="Medium"):
    task = Task(description, priority)
    self.tasks.append(task)
    self.save_tasks()
    return task
```

**complete_task() Hints:**
```python
def complete_task(self, task_id):
    for task in self.tasks:
        if task.id == task_id:
            task.completed = True
            self.save_tasks()
            return True
    return False
```

**save_tasks() Hints:**
```python
def save_tasks(self):
    try:
        task_data = [task.to_dict() for task in self.tasks]
        with open(self.filename, 'w') as f:
            json.dump(task_data, f, indent=2)
    except Exception as e:
        print(f"Error saving tasks: {e}")
```

**load_tasks() Hints:**
```python
def load_tasks(self):
    try:
        with open(self.filename, 'r') as f:
            task_data = json.load(f)
        self.tasks = [Task.from_dict(data) for data in task_data]
    except FileNotFoundError:
        self.tasks = []  # Start with empty list
    except Exception as e:
        print(f"Error loading tasks: {e}")
        self.tasks = []
```

### GUI Widget Creation

**create_widgets() Hints:**
```python
def create_widgets(self):
    # Title
    title_label = tk.Label(self.root, text="✅ My Todo List", 
                          font=("Arial", 16, "bold"))
    title_label.pack(pady=10)
    
    # Input frame
    input_frame = ttk.Frame(self.root)
    input_frame.pack(pady=5, padx=20, fill="x")
    
    # Task entry
    self.task_var = tk.StringVar()
    self.task_entry = ttk.Entry(input_frame, textvariable=self.task_var, width=30)
    self.task_entry.pack(side="left", padx=(0, 5))
    
    # Priority dropdown
    self.priority_var = tk.StringVar(value="Medium")
    priority_combo = ttk.Combobox(input_frame, textvariable=self.priority_var,
                                  values=["Low", "Medium", "High"], width=10)
    priority_combo.pack(side="left", padx=(0, 5))
    
    # Add button
    add_btn = ttk.Button(input_frame, text="Add Task", command=self.add_task)
    add_btn.pack(side="left")
    
    # Task list frame with scrollbar
    list_frame = ttk.Frame(self.root)
    list_frame.pack(pady=10, padx=20, fill="both", expand=True)
    
    # Canvas and scrollbar for task list
    self.canvas = tk.Canvas(list_frame, bg="white")
    scrollbar = ttk.Scrollbar(list_frame, orient="vertical", command=self.canvas.yview)
    self.scrollable_frame = ttk.Frame(self.canvas)
    
    self.canvas.configure(yscrollcommand=scrollbar.set)
    self.canvas_window = self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
    
    self.canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
    
    # Bind canvas resize
    self.scrollable_frame.bind("<Configure>", 
                              lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
    
    # Button frame
    button_frame = ttk.Frame(self.root)
    button_frame.pack(pady=5)
    
    clear_btn = ttk.Button(button_frame, text="Clear Completed", 
                          command=self.clear_completed_tasks)
    clear_btn.pack()
    
    # Status bar
    self.status_var = tk.StringVar()
    status_bar = ttk.Label(self.root, textvariable=self.status_var, relief="sunken")
    status_bar.pack(side="bottom", fill="x")
```

### Task Display

**refresh_task_list() Hints:**
```python
def refresh_task_list(self):
    # Clear existing widgets
    for widget in self.scrollable_frame.winfo_children():
        widget.destroy()
    
    # Get all tasks
    all_tasks = self.task_manager.tasks
    
    # Display each task
    for i, task in enumerate(all_tasks):
        task_frame = ttk.Frame(self.scrollable_frame)
        task_frame.pack(fill="x", padx=5, pady=2)
        
        # Checkbox
        var = tk.BooleanVar(value=task.completed)
        check = ttk.Checkbutton(task_frame, variable=var,
                               command=lambda t=task: self.on_task_toggle(t.id))
        check.pack(side="left")
        
        # Task description
        style = "overstrike" if task.completed else ""
        label = ttk.Label(task_frame, text=task.description, font=("Arial", 10, style))
        label.pack(side="left", padx=5)
        
        # Priority badge
        priority_colors = {"Low": "green", "Medium": "orange", "High": "red"}
        priority_label = tk.Label(task_frame, text=task.priority,
                                 fg=priority_colors.get(task.priority, "black"),
                                 font=("Arial", 8))
        priority_label.pack(side="left", padx=5)
        
        # Delete button
        delete_btn = ttk.Button(task_frame, text="🗑️", width=3,
                               command=lambda t=task: self.delete_task(t.id))
        delete_btn.pack(side="right")
    
    self.update_status()
```

### Event Handlers

**add_task() Handler Hints:**
```python
def add_task(self):
    description = self.task_var.get().strip()
    
    if not description:
        messagebox.showwarning("Empty Task", "Please enter a task description!")
        return
    
    priority = self.priority_var.get()
    self.task_manager.add_task(description, priority)
    
    # Clear input
    self.task_var.set("")
    self.task_entry.focus()
    
    # Refresh display
    self.refresh_task_list()
```

**on_task_toggle() Hints:**
```python
def on_task_toggle(self, task_id):
    task = next((t for t in self.task_manager.tasks if t.id == task_id), None)
    if task:
        task.completed = not task.completed
        self.task_manager.save_tasks()
        self.refresh_task_list()
```

### Keyboard Shortcuts

**bind_shortcuts() Hints:**
```python
def bind_shortcuts(self):
    # Enter key to add task
    self.task_entry.bind('<Return>', self.on_enter_pressed)
    
    # Ctrl+S to save (though we auto-save)
    self.root.bind('<Control-s>', lambda e: self.task_manager.save_tasks())
    
    # Escape to clear input
    self.root.bind('<Escape>', lambda e: self.task_var.set(""))
    
    # Set focus to entry on startup
    self.task_entry.focus()
```

### Status Updates

**update_status() Hints:**
```python
def update_status(self):
    active = len(self.task_manager.get_active_tasks())
    completed = len(self.task_manager.get_completed_tasks())
    total = len(self.task_manager.tasks)
    
    self.status_var.set(f"Tasks: {active} active, {completed} completed, {total} total")
```

### Common Issues and Solutions

**Issue: Lambda Variable Capture**
```python
# Wrong - all buttons will use the last task
for task in tasks:
    btn = ttk.Button(command=lambda: self.delete_task(task.id))

# Correct - capture task in lambda
for task in tasks:
    btn = ttk.Button(command=lambda t=task: self.delete_task(t.id))
```

**Issue: Canvas Scrolling**
```python
# Enable mouse wheel scrolling
def on_mousewheel(event):
    self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")

self.canvas.bind_all("<MouseWheel>", on_mousewheel)  # Windows
self.canvas.bind_all("<Button-4>", lambda e: self.canvas.yview_scroll(-1, "units"))  # Linux
self.canvas.bind_all("<Button-5>", lambda e: self.canvas.yview_scroll(1, "units"))   # Linux
```

**Issue: Window Resizing**
```python
# Make window resizable properly
self.root.rowconfigure(0, weight=1)
self.root.columnconfigure(0, weight=1)
```

### Styling and Polish

**Priority Color Coding:**
```python
def get_priority_color(priority):
    colors = {
        "Low": "#4CAF50",    # Green
        "Medium": "#FF9800",  # Orange  
        "High": "#F44336"     # Red
    }
    return colors.get(priority, "black")
```

**Task Strikethrough:**
```python
if task.completed:
    label.configure(font=("Arial", 10, "overstrike"), foreground="gray")
else:
    label.configure(font=("Arial", 10), foreground="black")
```

### Debugging Tips

1. **Print task data**:
   ```python
   print(f"Tasks: {[t.description for t in self.task_manager.tasks]}")
   ```

2. **Check file saving**:
   ```python
   print(f"Saving to: {self.task_manager.filename}")
   with open(self.task_manager.filename, 'r') as f:
       print(json.dumps(json.load(f), indent=2))
   ```

3. **Debug widget hierarchy**:
   ```python
   for child in self.scrollable_frame.winfo_children():
       print(f"Widget: {child.__class__.__name__}")
   ```

### Enhancement Ideas

**Add due dates:**
```python
self.due_date = due_date  # In Task.__init__
# Use tkcalendar or date entry widget
```

**Add categories:**
```python
self.category = category
# Use different colors or sections
```

**Add search/filter:**
```python
def filter_tasks(self, search_term):
    return [t for t in self.tasks 
            if search_term.lower() in t.description.lower()]
```

### AI Partnership Hints

**Good prompts to try:**
- "How do I create a scrollable frame in tkinter?"
- "What's the best way to handle task persistence in Python?"
- "How can I add drag-and-drop task reordering?"

**Remember:** Start with basic functionality, then add features!

