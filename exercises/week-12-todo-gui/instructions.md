# Week 12 Project: Todo GUI Application ✅

## Overview

Create a complete todo list application with a graphical user interface. This capstone project brings together everything you've learned: GUI development, file persistence, data management, and software architecture. You'll build a genuinely useful application!

## Learning Objectives

By completing this project, you will:
- ✓ Design complete GUI applications
- ✓ Implement full CRUD functionality
- ✓ Create professional user interfaces
- ✓ Apply software architecture principles
- ✓ Build production-ready applications

## Core Requirements (🟢 Basic)

Your todo application must:

1. **GUI Components**:
   - Task input field
   - Add task button
   - Task list display
   - Mark complete checkbox/button
   - Delete task button
   - Clear completed button

2. **Task Management**:
   - Add new tasks
   - Mark tasks as complete
   - Delete individual tasks
   - Clear all completed tasks
   - Display task count

3. **Data Persistence**:
   - Save tasks to file automatically
   - Load tasks on startup
   - Preserve task state (complete/incomplete)

4. **User Experience**:
   - Clear, intuitive interface
   - Keyboard shortcuts (Enter to add)
   - Visual feedback for actions
   - Error handling

5. **Task Properties**:
   - Task description
   - Creation timestamp
   - Completion status
   - Optional priority levels

### Example Interface
```
┌─────────────────────────────────────────────┐
│           ✅ My Todo List ✅                │
├─────────────────────────────────────────────┤
│                                             │
│  New Task: [_______________] [Add Task]     │
│                                             │
│  ─────────────────────────────────────      │
│                                             │
│  Tasks (3 active, 1 completed):             │
│                                             │
│  □ Buy groceries                     [X]    │
│  □ Complete Python project           [X]    │
│  ☑ Read Chapter 12                   [X]    │
│  □ Call mom                          [X]    │
│                                             │
│  [Clear Completed]  [Save]  [Load]          │
│                                             │
│  ─────────────────────────────────────      │
│  Status: 3 tasks remaining                  │
└─────────────────────────────────────────────┘
```

## Implementation Guide

### Step 1: GUI Layout Design
Plan your interface layout and components.

### Step 2: Task Data Structure
Design how tasks will be stored and managed.

### Step 3: Core Functionality
Implement add, complete, delete operations.

### Step 4: File Persistence
Add automatic saving and loading.

### Step 5: Polish and UX
Add keyboard shortcuts and visual feedback.

## GUI Structure Example

```python
import tkinter as tk
from tkinter import ttk

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Todo List")
        
        # Task entry
        self.task_var = tk.StringVar()
        self.entry = ttk.Entry(root, textvariable=self.task_var)
        
        # Buttons
        self.add_btn = ttk.Button(root, text="Add Task", command=self.add_task)
        
        # Task list
        self.task_listbox = tk.Listbox(root, selectmode=tk.SINGLE)
```

## Challenges

### 🟡 Intermediate Challenges

1. **Priority Levels**: High/Medium/Low with colors

2. **Due Dates**: Add deadlines to tasks

3. **Categories**: Organize tasks by project/type

4. **Search/Filter**: Find specific tasks

5. **Task Notes**: Add detailed descriptions

### 🔴 Advanced Challenges

1. **Drag and Drop**: Reorder tasks

2. **Multiple Lists**: Switch between different todo lists

3. **Statistics**: Show completion rates and trends

4. **Recurring Tasks**: Daily/weekly tasks

5. **Export Features**: Save as PDF or text

### 🟣 AI Partnership Challenge

1. **Architecture Design**:
   - Ask AI: "What's a good architecture for a todo app?"
   - Learn about MVC pattern
   - Implement clean separation of concerns

2. **Feature Planning**:
   - Get AI's input on useful todo features
   - Prioritize based on user needs
   - Design for extensibility

### ⭐ Reflection Exercise

Write a short paragraph answering:
- How did you organize your code for maintainability?
- What design decisions made the app user-friendly?
- How would you extend this for team collaboration?
- What did you learn about building complete applications?

## Testing Your Program

Test these scenarios:
- [ ] Tasks persist after closing app
- [ ] Can add tasks with Enter key
- [ ] Completed tasks show differently
- [ ] Delete removes correct task
- [ ] Clear completed works properly
- [ ] Empty task handling
- [ ] File corruption recovery

## Common Mistakes to Avoid

1. **No data validation** - Check empty tasks
2. **Poor event handling** - Bind events properly
3. **Inconsistent state** - Sync GUI and data
4. **No keyboard support** - Add shortcuts
5. **Ugly interface** - Use proper spacing

## Task Data Structure

```python
class Task:
    def __init__(self, description, priority="Medium"):
        self.id = self._generate_id()
        self.description = description
        self.priority = priority
        self.completed = False
        self.created_at = datetime.now()
        
    def to_dict(self):
        return {
            "id": self.id,
            "description": self.description,
            "priority": self.priority,
            "completed": self.completed,
            "created_at": self.created_at.isoformat()
        }
```

## AI Partnership Tips

### ✅ Good Prompts for Learning
- "What's the best way to structure a tkinter application?"
- "How should I handle task persistence in a todo app?"
- "What makes a todo app user-friendly?"

### ❌ Avoid These Prompts
- "Create a cloud-synced todo app"
- "Add AI task suggestions"
- "Build mobile app version"

## Event Handling Pattern

```python
# Bind Enter key to add task
self.entry.bind('<Return>', lambda e: self.add_task())

# Double-click to toggle completion
self.task_listbox.bind('<Double-Button-1>', self.toggle_task)

# Delete key to remove task
self.root.bind('<Delete>', self.delete_selected)
```

## Submission Checklist

Before considering your project complete:
- [ ] Clean, intuitive interface
- [ ] All CRUD operations work
- [ ] Tasks persist between sessions
- [ ] Keyboard shortcuts implemented
- [ ] Visual feedback for actions
- [ ] Proper error handling
- [ ] Code is well-organized
- [ ] App feels professional

## Extension Ideas

Once you've completed the basic requirements:
- Add task reminders/notifications
- Create subtasks functionality
- Add dark mode theme
- Implement task templates
- Create productivity statistics

## Resources

- Chapter 12: tkinter GUI development
- Chapter 13: Software architecture
- Chapter 9: File persistence
- Todo app best practices

---

Remember: This is your capstone project! You're building a real application that you can actually use. Make it great! 🚀✨

