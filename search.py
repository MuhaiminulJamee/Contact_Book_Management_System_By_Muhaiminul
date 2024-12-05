# search.py
def search_contacts(contacts):
    query = input("Enter name or phone number to search: ").strip()
    results = [contact for contact in contacts if query.lower() in contact.name.lower() or query in contact.phone]
    
    if results:
        print("\n--- Search Results ---")
        for contact in results:
            print(contact)
    else:
        print("No matching contacts found.")
