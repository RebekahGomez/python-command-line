from models import db, Contact

db.connect()
db.create_tables([Contact])

# Create a new contact
# contact = Contact(first_name='Joe', last_name='Schmoe', phone='555-123-4567')
# contact.save()
