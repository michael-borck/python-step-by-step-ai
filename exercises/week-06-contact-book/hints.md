# Contact Book - Hints 💡

## Stuck? Here are some hints to help you progress!

### General Structure Hints

**Hint 1: Dictionary Structure**
```python
# Each contact can be stored with name as key
contacts = {
    "John Doe": {
        "phone": "555-1234",
        "email": "john@email.com",
        "birthday": "01/15"
    }
}
```

**Hint 2: Getting User Input**
```python
# Always strip whitespace
name = input("Enter name: ").strip()

# Allow optional fields
phone = input("Phone (press Enter to skip): ").strip()
if not phone:
    phone = "N/A"
```

### Function-Specific Hints

**add_contact() Hints:**
- Check if name already exists: `if name in contacts:`
- Create nested dictionary for contact info
- Don't forget to handle empty name input

**view_all_contacts() Hints:**
- Check if dictionary is empty: `if not contacts:`
- Use enumerate for numbering: `for i, (name, info) in enumerate(contacts.items(), 1):`
- Format output nicely with indentation

**search_contact() Hints:**
- Make search case-insensitive: `search_name.lower()`
- Consider partial matching for intermediate challenge
- Handle "not found" case gracefully

**update_contact() Hints:**
- Show current values when asking for updates
- Allow keeping existing values (press Enter to skip)
- Update only fields that user wants to change

**delete_contact() Hints:**
- Always confirm before deleting
- Use `del contacts[name]` to remove
- Check existence first

### Common Issues and Solutions

**Issue: Case Sensitivity**
```python
# Store all names in title case
name = name.title()

# Or search case-insensitively
for contact_name in contacts:
    if search_name.lower() in contact_name.lower():
        # Found a match
```

**Issue: Empty Contact Book**
```python
if not contacts:
    print("No contacts yet. Add some!")
    return
```

**Issue: Invalid Menu Choice**
```python
if choice not in ["1", "2", "3", "4", "5", "6"]:
    print("Invalid choice!")
    continue
```

### Intermediate Challenge Hints

**Multiple Phone Numbers:**
```python
contact["phones"] = {
    "home": "555-1234",
    "work": "555-5678",
    "mobile": "555-9999"
}
```

**Sorting Contacts:**
```python
# Sort dictionary keys
sorted_names = sorted(contacts.keys())
for name in sorted_names:
    print(name, contacts[name])
```

**Partial Search:**
```python
# Find all contacts containing search term
matches = []
for name in contacts:
    if search_term.lower() in name.lower():
        matches.append(name)
```

### Debugging Tips

1. **Print statements help!**
   ```python
   print(f"DEBUG: contacts = {contacts}")
   ```

2. **Test with edge cases:**
   - Empty contact book
   - Single contact
   - Duplicate names
   - Empty fields

3. **Validate input early:**
   ```python
   if not name:
       print("Name cannot be empty!")
       return
   ```

### AI Partnership Hints

**Good prompts to try:**
- "How do I iterate through a nested dictionary in Python?"
- "What's the best way to update a value in a nested dictionary?"
- "How can I make string comparison case-insensitive?"

**Remember:** Start simple! Get basic add/view working before tackling search/update/delete.

