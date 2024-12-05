# file_handler.py
import csv
import os
from contact import Contact

def save_to_file(contacts, filename="contacts.csv"):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Email", "Phone", "Address"])
        for contact in contacts:
            writer.writerow([contact.name, contact.email, contact.phone, contact.address])

def load_from_file(filename="contacts.csv"):
    contacts = []
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                name, email, phone, address = row
                contacts.append(Contact(name, email, phone, address))
    return contacts
