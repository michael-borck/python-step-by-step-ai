#!/usr/bin/env python3
"""
Contact Book - Starter Code
Week 6 Project

TODO: Create a contact management system using dictionaries
"""

# Initialize your contacts dictionary here
contacts = {}

def display_menu():
    """Display the main menu options"""
    print("\n📞 Contact Book Manager 📞")
    print("========================")
    print("1. Add new contact")
    print("2. View all contacts")
    print("3. Search contact")
    print("4. Update contact")
    print("5. Delete contact")
    print("6. Exit")

def add_contact():
    """Add a new contact to the contact book"""
    # TODO: Get contact information from user
    # TODO: Check if contact already exists
    # TODO: Add contact to dictionary
    # TODO: Display success message
    pass

def view_all_contacts():
    """Display all contacts in the book"""
    # TODO: Check if contact book is empty
    # TODO: Display all contacts with their information
    # TODO: Show total number of contacts
    pass

def search_contact():
    """Search for a specific contact by name"""
    # TODO: Get search name from user
    # TODO: Check if contact exists
    # TODO: Display contact information if found
    # TODO: Show error message if not found
    pass

def update_contact():
    """Update an existing contact's information"""
    # TODO: Get contact name to update
    # TODO: Check if contact exists
    # TODO: Show current information
    # TODO: Get new information from user
    # TODO: Update the contact
    pass

def delete_contact():
    """Delete a contact from the book"""
    # TODO: Get contact name to delete
    # TODO: Check if contact exists
    # TODO: Confirm deletion with user
    # TODO: Delete the contact
    # TODO: Display success message
    pass

def main():
    """Main program loop"""
    print("Welcome to Contact Book Manager!")
    
    while True:
        display_menu()
        
        # TODO: Get user choice
        # TODO: Validate choice
        # TODO: Call appropriate function
        # TODO: Handle exit option
        
        choice = input("\nChoose an option (1-6): ")
        
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_all_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("\nThank you for using Contact Book Manager!")
            print("Goodbye! 👋")
            break
        else:
            print("❌ Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
