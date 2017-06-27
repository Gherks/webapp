from database import db, Contact


for entry in Contact.select():
    print(entry.first_name, entry.last_name, entry.miscellaneous)
