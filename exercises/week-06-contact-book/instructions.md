# Week 6 Project: Contact Book 📞

## Overview

Create a contact management system using dictionaries. This project teaches you how to organize complex data with nested dictionaries and perform CRUD (Create, Read, Update, Delete) operations. You'll build a practical application that could actually be useful!

## Learning Objectives

By completing this project, you will:
- ✓ Work with dictionaries to store structured data
- ✓ Create nested data structures
- ✓ Implement CRUD operations
- ✓ Build menu-driven applications with functions
- ✓ Handle data validation and error cases

## Core Requirements (🟢 Basic)

Your contact book must:

1. **Store contact information** using dictionaries:
   - Name (required)
   - Phone number
   - Email address
   - Birthday

2. **Provide a menu** with these options:
   - Add new contact
   - View all contacts
   - Search for a contact
   - Update contact information
   - Delete a contact
   - Exit program

3. **Use functions** for each operation

4. **Validate inputs** (e.g., check if contact exists before updating)

5. **Display contacts** in a readable format

### Example Interaction
```
📞 Contact Book Manager 📞
========================

1. Add new contact
2. View all contacts
3. Search contact
4. Update contact
5. Delete contact
6. Exit

Choose an option (1-6): 1

--- Add New Contact ---
Name: Alice Johnson
Phone: 555-1234
Email: alice@email.com
Birthday (MM/DD): 03/15

✅ Contact added successfully!

Choose an option (1-6): 2

--- All Contacts ---
1. Alice Johnson
   📱 555-1234
   📧 alice@email.com
   🎂 03/15

Total contacts: 1

Choose an option (1-6): 3

--- Search Contact ---
Enter name to search: Alice
Found: Alice Johnson
   📱 555-1234
   📧 alice@email.com
   🎂 03/15
```

## Implementation Guide

### Step 1: Design Data Structure
Decide how to organize contacts in a dictionary. Consider using names as keys.

### Step 2: Create Core Functions
- `add_contact()` - Add new contact to book
- `view_all_contacts()` - Display all contacts
- `search_contact()` - Find specific contact
- `update_contact()` - Modify existing contact
- `delete_contact()` - Remove contact

### Step 3: Build Menu System
Create a main loop that displays options and calls appropriate functions.

### Step 4: Add Input Validation
Ensure the program handles missing contacts, duplicate names, and empty inputs.

### Step 5: Format Output
Make the contact display clean and easy to read.

## Data Structure Example

```python
# Simple structure
contacts = {
    "Alice Johnson": {
        "phone": "555-1234",
        "email": "alice@email.com",
        "birthday": "03/15"
    },
    "Bob Smith": {
        "phone": "555-5678",
        "email": "bob@email.com",
        "birthday": "07/22"
    }
}
```

## Challenges

### 🟡 Intermediate Challenges

1. **Multiple Phone Numbers**: Allow contacts to have home, work, and mobile numbers

2. **Case-Insensitive Search**: Make searches work regardless of capitalization

3. **Partial Name Search**: Find contacts by typing part of their name

4. **Sort Contacts**: Display contacts alphabetically

5. **Contact Groups**: Add categories like "Family", "Friends", "Work"

### 🔴 Advanced Challenges

1. **Save to File**: Persist contacts between program runs using JSON

2. **Import/Export**: Add CSV import/export functionality

3. **Birthday Reminders**: Show upcoming birthdays

4. **Duplicate Detection**: Warn when adding similar names

5. **Contact History**: Track when contacts were added/modified

### 🟣 AI Partnership Challenge

1. **Data Structure Design**:
   - Ask AI: "What are different ways to structure contact data in Python?"
   - Compare dictionary vs list of dictionaries
   - Choose the most appropriate for your needs

2. **Search Implementation**:
   - Get AI's approach to fuzzy searching
   - Implement basic version first
   - Add sophistication gradually

### ⭐ Reflection Exercise

Write a short paragraph answering:
- Why are dictionaries good for storing contact information?
- How did you handle the case when a contact doesn't exist?
- What would you add to make this a "real" contact app?
- How is this different from a list-based approach?

## Testing Your Program

Test these scenarios:
- [ ] Add multiple contacts successfully
- [ ] View contacts when book is empty
- [ ] Search for existing and non-existing contacts
- [ ] Update each field of a contact
- [ ] Delete a contact and verify it's gone
- [ ] Handle duplicate names appropriately
- [ ] Exit cleanly

## Common Mistakes to Avoid

1. **Overwriting contacts** - Check if name exists before adding
2. **Case sensitivity** - "alice" vs "Alice" causing issues
3. **Empty dictionary access** - Handle when no contacts exist
4. **Not validating input** - Empty names or invalid choices
5. **Poor menu flow** - Returning to menu after each operation

## Dictionary Operations Reference

```python
# Adding/updating
contacts[name] = {"phone": phone, "email": email}

# Checking existence
if name in contacts:
    # Contact exists

# Deleting
if name in contacts:
    del contacts[name]

# Iterating
for name, info in contacts.items():
    print(f"{name}: {info['phone']}")
```

## AI Partnership Tips

### ✅ Good Prompts for Learning
- "How do I check if a key exists in a dictionary?"
- "What's the best way to update nested dictionary values?"
- "How can I make dictionary searches case-insensitive?"

### ❌ Avoid These Prompts
- "Create a full contact management system with GUI"
- "Add facial recognition to contacts"
- "Integrate with phone's actual contact list"

## Input Validation Pattern

```python
def get_contact_name():
    while True:
        name = input("Enter name: ").strip()
        if name:
            return name
        print("Name cannot be empty. Try again.")
```

## Submission Checklist

Before considering your project complete:
- [ ] All CRUD operations work correctly
- [ ] Menu system is clear and easy to use
- [ ] Functions are properly organized
- [ ] Input validation prevents crashes
- [ ] Contacts display in readable format
- [ ] Search function finds contacts
- [ ] Program exits cleanly
- [ ] Code uses dictionaries effectively

## Extension Ideas

Once you've completed the basic requirements:
- Add address information with multiple fields
- Create contact favorites/starred contacts
- Add notes field for each contact
- Implement contact search by any field
- Create backup and restore functions

## Resources

- Chapter 8: Dictionary operations
- Chapter 6: Functions review
- Python docs: Dictionary methods
- Chapter 8: Nested data structures

---

Remember: This project combines functions and dictionaries - two powerful Python features. Master this, and you're ready for real-world data management! 📚✨
