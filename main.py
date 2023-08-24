import argparse
from models import db, Contact


# CREATE NEW CONTACT
def create_contact(first_name, last_name, phone):
    db.connect()
    # .create() is a shorthand method for creating and saving a model instance so we don't need contact.save() after creating a new contact
    contact = Contact.create(first_name=first_name,
                             last_name=last_name, phone=phone)
    db.close()
    print(f"Contact {contact.first_name} {contact.last_name} created!")


# LIST ALL CONTACTS
def list_contacts():
    db.connect()
    # The .select() method returns a query object that we can iterate over to get all the contacts in the database.
    for contact in Contact.select():
        print(f"{contact.first_name} {contact.last_name} {contact.phone}")
    db.close()


# UPDATE CONTACT'S PHONE NUMBER USING FIRST AND LAST NAME
def update_contact(first_name, last_name, phone):
    db.connect()
    try:
        contact = Contact.get((Contact.first_name ==
                              first_name) & (Contact.last_name == last_name))
        contact.phone = phone
        contact.save()
        print(f"Contact {contact.first_name} {contact.last_name} updated!")
    except Contact.DoesNotExist:
        print("Contact not found!")
    db.close()


# FIND ONE CONTACT
def find_contact(first_name, last_name):
    db.connect()
    try:
        contact = Contact.get((Contact.first_name == first_name) & (
            Contact.last_name == last_name))
        print(f"{contact.first_name} {contact.last_name} {contact.phone}")
        # .DoesNotExist is a built-in PeeWee exception that is raised when a query returns no results.
    except Contact.DoesNotExist:
        print("Contact not found!")
    db.close()


# DELETE CONTACT
def delete_contact(first_name, last_name):
    db.connect()
    try:
        contact = Contact.get((Contact.first_name == first_name) & (
            Contact.last_name == last_name))
        contact.delete_instance()
        print(f"Contact {contact.first_name} {contact.last_name} deleted!")
    except Contact.DoesNotExist:
        print("Contact not found!")
    db.close()
