# contact_manager.py
from contact import Contact
from file_handler import save_to_file
from search import search_contacts
from error_handling import handle_invalid_input

def add_contact(contacts):
    print("\nAdd a new contact:")
    name = input("Name: ").strip()
    while not name.isalpha():
        print("Name must be a string. Please try again.")
        name = input("Name: ").strip()

    email = input("Email: ").strip()
    phone_number = input("Phone Number: ").strip()
    
    # phone number unique or not testing
    if any(contact.phone == phone_number for contact in contacts):
        print("This phone number is already in use. Try again.")
        return

    address = input("Address: ").strip()
    
    new_contact = Contact(name, email, phone_number, address)
    contacts.append(new_contact)
    
    save_to_file(contacts) # saving

    print(f"Contact for {name} added successfully!")

def view_contacts(contacts):
    if not contacts:
        print("No contacts available.")
    else:
        print("\n--- All Contacts ---")
        for contact in contacts:
            print(contact)

def remove_contact(contacts):
    phone_number = input("Enter the phone number of the contact to remove: ").strip()
    contact_to_remove = next((contact for contact in contacts if contact.phone == phone_number), None)
    
    if contact_to_remove:
        contacts.remove(contact_to_remove)
        print(f"Contact {contact_to_remove.name} removed successfully.")
        save_to_file(contacts)
    else:
        print("Contact not found.")

def search_contact(contacts):
    search_contacts(contacts)  # Calling the search function for searching contact
