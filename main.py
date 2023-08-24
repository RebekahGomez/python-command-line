from models import db, Contact


# Turns out I don't need separate functions for this project, but I don't want to erase the work I did, even if it was accidentally the wrong work
# CREATE NEW CONTACT
# def create_contact(first_name, last_name, phone):
#     db.connect()
#     # .create() is a shorthand method for creating and saving a model instance so we don't need contact.save() after creating a new contact
#     contact = Contact.create(first_name=first_name,
#                              last_name=last_name, phone=phone)
#     db.close()
#     print(f"Contact {contact.first_name} {contact.last_name} created!")


# # LIST ALL CONTACTS
# def list_contacts():
#     db.connect()
#     # The .select() method returns a query object that we can iterate over to get all the contacts in the database.
#     for contact in Contact.select():
#         print(f"{contact.first_name} {contact.last_name} {contact.phone}")
#     db.close()


# # UPDATE CONTACT'S PHONE NUMBER USING FIRST AND LAST NAME
# def update_contact(first_name, last_name, phone):
#     db.connect()
#     try:
#         contact = Contact.get((Contact.first_name ==
#                               first_name) & (Contact.last_name == last_name))
#         contact.phone = phone
#         contact.save()
#         print(f"Contact {contact.first_name} {contact.last_name} updated!")
#     except Contact.DoesNotExist:
#         print("Contact not found!")
#     db.close()


# # FIND ONE CONTACT
# def find_contact(first_name, last_name):
#     db.connect()
#     try:
#         contact = Contact.get((Contact.first_name == first_name) & (
#             Contact.last_name == last_name))
#         print(f"{contact.first_name} {contact.last_name} {contact.phone}")
#         # .DoesNotExist is a built-in PeeWee exception that is raised when a query returns no results.
#     except Contact.DoesNotExist:
#         print("Contact not found!")
#     db.close()


# # DELETE CONTACT
# def delete_contact(first_name, last_name):
#     db.connect()
#     try:
#         contact = Contact.get((Contact.first_name == first_name) & (
#             Contact.last_name == last_name))
#         contact.delete_instance()
#         print(f"Contact {contact.first_name} {contact.last_name} deleted!")
#     except Contact.DoesNotExist:
#         print("Contact not found!")
#     db.close()


# # MAIN FUNCTION
# def main():
#     parser = argparse.ArgumentParser(description="Manage your contacts")
#     subparsers = parser.add_subparsers(dest="command")

#     # CREATE SUBPARSER
#     create_parser = subparsers.add_parser(
#         "create", help="Create a new contact")
#     create_parser.add_argument("first_name", help="Contact's first name")
#     create_parser.add_argument("last_name", help="Contact's last name")
#     create_parser.add_argument("phone", help="Contact's phone number")
