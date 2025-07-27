# Week 7 Project: Journal App 📔

## Overview

Create a personal journal application that saves entries to files. This project teaches file input/output operations, data persistence, and working with dates/timestamps. You'll build a practical app that maintains your thoughts across program runs!

## Learning Objectives

By completing this project, you will:
- ✓ Read and write text files
- ✓ Handle file operations safely
- ✓ Work with dates and timestamps
- ✓ Create persistent data storage
- ✓ Format and organize file data

## Core Requirements (🟢 Basic)

Your journal app must:

1. **Create journal entries** with:
   - Entry content (multi-line text)
   - Automatic timestamp
   - Entry number/ID

2. **Save entries to a file** that persists between runs

3. **View all entries** from the file

4. **Search entries** by date or keyword

5. **Handle file operations safely** (create if doesn't exist)

6. **Provide a clean menu interface**

### Example Interaction
```
📔 Personal Journal 📔
===================

1. Write new entry
2. View all entries
3. Search entries
4. Exit

Choose option (1-4): 1

--- New Journal Entry ---
Write your entry (type 'DONE' on a new line when finished):
Today was a great day! I learned about file I/O in Python.
I can now save data that persists between program runs.
This opens up so many possibilities!
DONE

✅ Entry saved! (Entry #1)

Choose option (1-4): 2

--- All Journal Entries ---

Entry #1 - 2024-01-15 14:30:45
--------------------------------
Today was a great day! I learned about file I/O in Python.
I can now save data that persists between program runs.
This opens up so many possibilities!

Total entries: 1
```

## Implementation Guide

### Step 1: File Setup
Decide on file format and create/open journal file.

### Step 2: Entry Creation
Get multi-line input and add timestamp.

### Step 3: File Writing
Append new entries to the journal file.

### Step 4: File Reading
Read and parse entries from the file.

### Step 5: Search Function
Implement searching through file contents.

## File Format Example

```
=== Entry 1 ===
Date: 2024-01-15 14:30:45
Today was a great day! I learned about file I/O in Python.
I can now save data that persists between program runs.
This opens up so many possibilities!

=== Entry 2 ===
Date: 2024-01-16 09:15:22
Started working on the journal project today.
File operations are easier than I thought!
```

## Challenges

### 🟡 Intermediate Challenges

1. **Entry Tags**: Add categories/tags to entries (#work, #personal)

2. **Date Range Search**: View entries between two dates

3. **Entry Statistics**: Show total entries, words, most active days

4. **Edit Entries**: Allow modifying existing entries

5. **Export Feature**: Save entries to different formats (HTML, PDF-ready)

### 🔴 Advanced Challenges

1. **Multiple Journals**: Support different journal files

2. **Encryption**: Add password protection to journal

3. **Backup System**: Automatic backups with timestamp

4. **Entry Templates**: Pre-formatted entries for different types

5. **Mood Tracking**: Add mood indicators and analytics

### 🟣 AI Partnership Challenge

1. **File Format Design**:
   - Ask AI: "What are different ways to structure journal entries in a text file?"
   - Compare JSON vs custom format
   - Choose based on readability and ease of parsing

2. **Search Implementation**:
   - Get AI's approach to text searching
   - Implement both date and keyword search
   - Handle case-insensitive searching

### ⭐ Reflection Exercise

Write a short paragraph answering:
- Why is file I/O important for real applications?
- How did you handle the case when the journal file doesn't exist?
- What challenges did you face with multi-line input?
- How would you extend this to support images or formatting?

## Testing Your Program

Test these scenarios:
- [ ] First run creates new journal file
- [ ] Entries persist after closing program
- [ ] Multi-line entries work correctly
- [ ] Empty entries are handled
- [ ] Search finds correct entries
- [ ] File errors are handled gracefully
- [ ] Timestamps are accurate

## Common Mistakes to Avoid

1. **Not closing files** - Use `with` statement
2. **Overwriting instead of appending** - Use mode 'a' not 'w'
3. **No error handling** - Check if file exists
4. **Poor date formatting** - Use consistent format
5. **Lost line breaks** - Preserve entry formatting

## File Operations Reference

```python
# Safe file reading
try:
    with open("journal.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    content = ""

# Safe file writing (append)
with open("journal.txt", "a") as file:
    file.write(entry)

# Getting timestamp
from datetime import datetime
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
```

## AI Partnership Tips

### ✅ Good Prompts for Learning
- "How do I safely read a file that might not exist?"
- "What's the best way to get multi-line input in Python?"
- "How can I search for text within a file?"

### ❌ Avoid These Prompts
- "Create a cloud-synced journal with database"
- "Add rich text editing with formatting"
- "Implement voice-to-text journal entries"

## Multi-line Input Pattern

```python
print("Write your entry (type 'DONE' when finished):")
lines = []
while True:
    line = input()
    if line.upper() == "DONE":
        break
    lines.append(line)
entry = "\n".join(lines)
```

## Submission Checklist

Before considering your project complete:
- [ ] Entries save to file successfully
- [ ] File persists between program runs
- [ ] Timestamps are automatically added
- [ ] Can view all previous entries
- [ ] Search function works
- [ ] Multi-line entries preserve formatting
- [ ] File errors handled gracefully
- [ ] Clean menu interface

## Extension Ideas

Once you've completed the basic requirements:
- Add word count for each entry
- Create monthly/yearly summaries
- Add weather information to entries
- Implement entry reminders
- Create journal entry prompts

## Resources

- Chapter 9: File I/O operations
- Python docs: datetime module
- Chapter 9: Error handling with files
- String methods for searching

---

Remember: A journal is only useful if it saves your thoughts! Focus on reliable file operations and data persistence. 💾✨

