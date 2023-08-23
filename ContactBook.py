list_of_contacts = []
import sqlite3

# Establish a connection to the database
conn = sqlite3.connect('contacts.db')
cursor = conn.cursor()

# Create a table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS contacts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        phone_number TEXT,
        email TEXT,
        address TEXT
    )
''')
conn.commit()

# Define a list to store contacts
list_of_contacts = []

while True:
    print("Contacts")
    option = int(input("Enter\n1 to Create a contact.\n2 to Update a contact.\n3 to View Contact list\n4 to Delete a contact\n5 to Exit the program\n"))
    
    if option == 1:
        try:
            Contact = {}
            while True:
                name = input("Enter the name: ").capitalize()
                if len(name) == 0:
                    print("Please enter a name.")
                else:
                    Contact["Name"] = name
                    break
            while True:
                phone_no = input("Enter the phone number: ")
                if len(phone_no) != 10:
                    print("Please enter a 10-digit number.")
                else:
                    Contact["Phone_Number"] = phone_no
                    break
            while True:
                email = input("Enter email: ")
                if '@' not in email or '.com' not in email:
                    print("Please enter a valid email.")
                else:
                    Contact["Email"] = email
                    break
            while True:
                address = input("Enter address: ")
                if len(address) == 0:
                    print("Empty address is invalid. Please enter an address.")
                else:
                    Contact["Address"] = address
                    break

            list_of_contacts.append(Contact)

            # Insert contact data into the SQL table
            cursor.execute('INSERT INTO contacts (name, phone_number, email, address) VALUES (?, ?, ?, ?)',
                           (Contact["Name"], Contact["Phone_Number"], Contact["Email"], Contact["Address"]))
            conn.commit()

            print("Contact added successfully!")

        except ValueError:
            print("Invalid input. Please enter valid values.")

    if option == 2:
        Needupdate = input("Enter the name: ").capitalize()
        found = False
        for contact in list_of_contacts:
            if contact["Name"] == Needupdate:
                Toupdate = input("Enter what you want to update (Name, PhoneNumber, Email, Address): ").capitalize()

                if Toupdate == "Name":
                    new_name = input("Enter the new name: ")
                    if len(new_name) == 0:
                        print("Please enter a valid name.")
                    else:
                        contact["Name"] = new_name
                        print("Name updated successfully!")

                elif Toupdate == "PhoneNumber":
                    new_phone = input("Enter the new phone number: ")
                    if len(new_phone) != 10:
                        print("Please enter a valid 10-digit phone number.")
                    else:
                        contact["Phone_Number"] = new_phone
                        print("Phone number updated successfully!")

                elif Toupdate == "Email":
                    new_email = input("Enter the new email: ")
                    if '@' not in new_email or '.com' not in new_email:
                        print("Please enter a valid email.")
                    else:
                        contact["Email"] = new_email
                        print("Email updated successfully!")

                elif Toupdate == "Address":
                    new_address = input("Enter the new address: ")
                    if len(new_address) == 0:
                        print("Please enter a valid address.")
                    else:
                        contact["Address"] = new_address
                        print("Address updated successfully!")

                else:
                    print("Invalid update option. Please choose from Name, PhoneNumber, Email, or Address.")
                
                found = True
                break
        
        if not found:
            print("Contact not found.")

    if option == 3:
        # Retrieve and display contacts from the SQL table
        cursor.execute('SELECT * FROM contacts')
        rows = cursor.fetchall()
        for row in rows:
            print(row)

    if option == 4:
        contact_name = input("Enter the name of the contact to delete: ").capitalize()
        cursor.execute('DELETE FROM contacts WHERE name = ?', (contact_name,))
        conn.commit()
        print(f"Contact '{contact_name}' deleted successfully.")

    if option == 5:
        break

# Close the database connection
conn.close()

    


