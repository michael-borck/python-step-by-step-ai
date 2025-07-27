#!/usr/bin/env python3
"""
Journal App - Starter Code
Week 7 Project

TODO: Create a journal application with file persistence
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
    
    # TODO: Get multi-line input from user
    # TODO: Create timestamp
    # TODO: Format entry with entry number
    # TODO: Append to journal file
    # TODO: Display success message
    pass

def view_entries():
    """View all journal entries"""
    print("\n--- All Journal Entries ---")
    
    # TODO: Check if journal file exists
    # TODO: Read all entries from file
    # TODO: Display each entry nicely formatted
    # TODO: Show total number of entries
    pass

def search_entries():
    """Search for entries by keyword or date"""
    print("\n--- Search Entries ---")
    
    # TODO: Get search term from user
    # TODO: Read journal file
    # TODO: Search for matching entries
    # TODO: Display matching entries
    # TODO: Handle no matches found
    pass

def get_multiline_input():
    """Get multi-line input from user"""
    print("Write your entry (type 'DONE' on a new line when finished):")
    
    lines = []
    # TODO: Implement multi-line input collection
    # TODO: Stop when user types 'DONE'
    # TODO: Return joined lines
    
    return ""  # Placeholder

def count_entries():
    """Count the number of entries in the journal"""
    # TODO: Read file and count entries
    # TODO: Return the count
    return 0  # Placeholder

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

