#!/usr/bin/env python3
"""
Contact Book - Basic Solution
Week 6 Project

A simple contact management system using dictionaries.
This solution implements all core requirements.
"""

# Global dictionary to store contacts
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
    print("\n--- Add New Contact ---")
    
    # Get contact name
    name = input("Name: ").strip()
    if not name:
        print("❌ Name cannot be empty!")
        return
    
    # Check if contact already exists
    if name in contacts:
        print(f"❌ Contact '{name}' already exists!")
        return
    
    # Get contact information
    phone = input("Phone: ").strip()
    email = input("Email: ").strip()
    birthday = input("Birthday (MM/DD): ").strip()
    
    # Add contact to dictionary
    contacts[name] = {
        "phone": phone if phone else "N/A",
        "email": email if email else "N/A",
        "birthday": birthday if birthday else "N/A"
    }
    
    print(f"\n✅ Contact '{name}' added successfully!")

def view_all_contacts():
    """Display all contacts in the book"""
    print("\n--- All Contacts ---")
    
    if not contacts:
        print("No contacts in your book yet.")
        return
    
    # Display each contact
    for i, (name, info) in enumerate(contacts.items(), 1):
        print(f"\n{i}. {name}")
        print(f"   📱 {info['phone']}")
        print(f"   📧 {info['email']}")
        print(f"   🎂 {info['birthday']}")
    
    print(f"\nTotal contacts: {len(contacts)}")

def search_contact():
    """Search for a specific contact by name"""
    print("\n--- Search Contact ---")
    
    if not contacts:
        print("No contacts to search.")
        return
    
    search_name = input("Enter name to search: ").strip()
    if not search_name:
        print("❌ Search name cannot be empty!")
        return
    
    # Search for exact match
    if search_name in contacts:
        info = contacts[search_name]
        print(f"\nFound: {search_name}")
        print(f"   📱 {info['phone']}")
        print(f"   📧 {info['email']}")
        print(f"   🎂 {info['birthday']}")
    else:
        print(f"❌ Contact '{search_name}' not found.")

def update_contact():
    """Update an existing contact's information"""
    print("\n--- Update Contact ---")
    
    if not contacts:
        print("No contacts to update.")
        return
    
    name = input("Enter contact name to update: ").strip()
    if not name:
        print("❌ Name cannot be empty!")
        return
    
    if name not in contacts:
        print(f"❌ Contact '{name}' not found.")
        return
    
    # Show current information
    info = contacts[name]
    print(f"\nCurrent information for {name}:")
    print(f"   📱 Phone: {info['phone']}")
    print(f"   📧 Email: {info['email']}")
    print(f"   🎂 Birthday: {info['birthday']}")
    
    print("\nEnter new information (press Enter to keep current):")
    
    # Get new information
    new_phone = input(f"New phone [{info['phone']}]: ").strip()
    new_email = input(f"New email [{info['email']}]: ").strip()
    new_birthday = input(f"New birthday [{info['birthday']}]: ").strip()
    
    # Update only if new value provided
    if new_phone:
        contacts[name]['phone'] = new_phone
    if new_email:
        contacts[name]['email'] = new_email
    if new_birthday:
        contacts[name]['birthday'] = new_birthday
    
    print(f"\n✅ Contact '{name}' updated successfully!")

def delete_contact():
    """Delete a contact from the book"""
    print("\n--- Delete Contact ---")
    
    if not contacts:
        print("No contacts to delete.")
        return
    
    name = input("Enter contact name to delete: ").strip()
    if not name:
        print("❌ Name cannot be empty!")
        return
    
    if name not in contacts:
        print(f"❌ Contact '{name}' not found.")
        return
    
    # Confirm deletion
    confirm = input(f"Are you sure you want to delete '{name}'? (yes/no): ").lower()
    if confirm == 'yes':
        del contacts[name]
        print(f"\n✅ Contact '{name}' deleted successfully!")
    else:
        print("Deletion cancelled.")

def main():
    """Main program loop"""
    print("Welcome to Contact Book Manager!")
    
    while True:
        display_menu()
        
        choice = input("\nChoose an option (1-6): ").strip()
        
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