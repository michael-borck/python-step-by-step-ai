#!/usr/bin/env python3
"""
Journal App - Basic Solution
Week 7 Project

A simple journal application with file persistence.
This solution implements all core requirements.
"""

from datetime import datetime

# Constants
JOURNAL_FILE = "my_journal.txt"

def display_menu():
    """Display the main menu"""
    print("\n📔 Personal Journal 📔")
    print("===================")
    print("1. Write new entry")
    print("2. View all entries")
    print("3. Search entries")
    print("4. Exit")

def write_entry():
    """Write a new journal entry"""
    print("\n--- New Journal Entry ---")
    
    # Get multi-line input
    entry_content = get_multiline_input()
    
    if not entry_content.strip():
        print("❌ Entry cannot be empty!")
        return
    
    # Get current timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Count existing entries to get entry number
    entry_number = count_entries() + 1
    
    # Format entry
    formatted_entry = f"""=== Entry {entry_number} ===
Date: {timestamp}
{entry_content}

"""
    
    # Append to journal file
    with open(JOURNAL_FILE, "a") as f:
        f.write(formatted_entry)
    
    print(f"\n✅ Entry saved! (Entry #{entry_number})")

def view_entries():
    """View all journal entries"""
    print("\n--- All Journal Entries ---")
    
    try:
        with open(JOURNAL_FILE, "r") as f:
            content = f.read()
    except FileNotFoundError:
        print("No entries yet. Start writing!")
        return
    
    if not content.strip():
        print("No entries yet. Start writing!")
        return
    
    # Display all content
    print(content)
    
    # Count entries
    entry_count = content.count("=== Entry")
    print(f"Total entries: {entry_count}")

def search_entries():
    """Search for entries by keyword or date"""
    print("\n--- Search Entries ---")
    
    try:
        with open(JOURNAL_FILE, "r") as f:
            content = f.read()
    except FileNotFoundError:
        print("No entries to search.")
        return
    
    if not content.strip():
        print("No entries to search.")
        return
    
    search_term = input("Enter search keyword or date (YYYY-MM-DD): ").strip().lower()
    if not search_term:
        print("❌ Search term cannot be empty!")
        return
    
    # Split into individual entries
    entries = content.split("=== Entry")
    # Remove empty first element
    entries = entries[1:] if entries else []
    
    found_entries = []
    
    for i, entry in enumerate(entries):
        # Check if search term is in entry (case insensitive)
        if search_term in entry.lower():
            found_entries.append(f"=== Entry{entry}")
    
    if found_entries:
        print(f"\nFound {len(found_entries)} matching entries:\n")
        for entry in found_entries:
            print(entry)
    else:
        print(f"❌ No entries found containing '{search_term}'")

def get_multiline_input():
    """Get multi-line input from user"""
    print("Write your entry (type 'DONE' on a new line when finished):")
    
    lines = []
    while True:
        line = input()
        if line.upper() == "DONE":
            break
        lines.append(line)
    
    return "\n".join(lines)

def count_entries():
    """Count the number of entries in the journal"""
    try:
        with open(JOURNAL_FILE, "r") as f:
            content = f.read()
        return content.count("=== Entry")
    except FileNotFoundError:
        return 0

def main():
    """Main program loop"""
    print("Welcome to your Personal Journal!")
    
    while True:
        display_menu()
        
        choice = input("\nChoose option (1-4): ").strip()
        
        if choice == "1":
            write_entry()
        elif choice == "2":
            view_entries()
        elif choice == "3":
            search_entries()
        elif choice == "4":
            print("\nClosing journal. Your thoughts are saved!")
            print("Goodbye! 📖")
            break
        else:
            print("❌ Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()

