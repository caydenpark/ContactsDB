import os
import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account.
cred = credentials.Certificate('contacts-780bb-firebase-adminsdk-iklaa-51ff7353ff.json')
app = firebase_admin.initialize_app(cred)
db = firestore.client()

def addContact():
    # Get user input for contact details
    fName = input("\nFirst Name: ")
    lName = input("Last Name: ")
    email = input("Email: ")
    phone = input("Phone Number: ")

    # Create a document reference with the first name as the document ID
    doc_ref = db.collection("Persons").document(fName)

    doc_ref.set({
        "First Name":fName,
        "Last Name":lName,
        "Email":email,
        "Phone":phone
    })

    print(f"\n{fName}'s contact has been added")

    input("\nPress enter to return to the menu.")
    os.system('clear')

def updateContact():
    contact_to_update = input("\nEnter the name of the person whose contact you wish to update: ")

    # Check if the contact exists in the database
    doc_ref = db.collection("Persons").document(contact_to_update)
    doc = doc_ref.get()

    if doc.exists:
        # Display current contact information
        print(f"\nCurrent Contact Info for {contact_to_update}:\n")
        contact_info = doc.to_dict()
        print(f"First Name: {contact_info.get('First Name', 'N/A')}")
        print(f" Last Name: {contact_info.get('Last Name', 'N/A')}")
        print(f"     Email: {contact_info.get('Email', 'N/A')}")
        print(f"     Phone: {contact_info.get('Phone', 'N/A')}")

        # Get updated contact details or keep them the same
        new_fName = input("\nEnter new First Name (press enter to keep it unchanged): ") or contact_info.get('First Name', '')
        new_lName = input("Enter new Last Name (press enter to keep it unchanged): ") or contact_info.get('Last Name', '')
        new_email = input("Enter new Email (press enter to keep it unchanged): ") or contact_info.get('Email', '')
        new_phone = input("Enter new Phone Number (press enter to keep it unchanged): ") or contact_info.get('Phone', '')

        # Update the contact in the database
        doc_ref.set({
            "First Name": new_fName,
            "Last Name": new_lName,
            "Email": new_email,
            "Phone": new_phone
        })

        print(f"\n{contact_to_update}'s contact has been updated")
    else:
        print(f'\nSorry, there is no contact for "{contact_to_update}".')

    input("\nPress enter to return to the menu.")
    os.system('clear')

def deleteContact():
    contact_to_delete = input("\nEnter the name of the person whose contact you wish to delete: ")

    # Check if the contact exists in the database
    doc_ref = db.collection("Persons").document(contact_to_delete)
    doc = doc_ref.get()

    if doc.exists:
        doc_ref.delete()
        print(f"\n{contact_to_delete}'s contact has been deleted")
    else:
        print(f'\nSorry, there is no contact for "{contact_to_delete}".')

    input("\nPress enter to return to the menu.")
    os.system('clear')

def displayContact():
    contact_name = input("\nEnter the name of the person whose contact you wish to display: ")
    
    # Retrieve the contact details from the database
    doc_ref = db.collection("Persons").document(contact_name)
    doc = doc_ref.get()

    if doc.exists:
        contact_info = doc.to_dict()
        print(f"\n{contact_name}'s Contact Info:\n")
        print(f"First Name: {contact_info.get('First Name', 'N/A')}")
        print(f" Last Name: {contact_info.get('Last Name', 'N/A')}")
        print(f"     Email: {contact_info.get('Email', 'N/A')}")
        print(f"     Phone: {contact_info.get('Phone', 'N/A')}")
    else:
        print(f'\nSorry, there is no contact for "{contact_name}".')
        
    input("\nPress enter to return to the menu.")
    os.system('clear')

def displayAllContacts():
    # Retrieve all contacts from the database
    users_ref = db.collection("Persons")
    docs = users_ref.stream()

    print("\nAll Contacts:")
    for doc in docs:
        contact_info = doc.to_dict()
        print(f"\nFirst Name: {contact_info.get('First Name', 'N/A')}")
        print(f" Last Name: {contact_info.get('Last Name', 'N/A')}")
        print(f"     Email: {contact_info.get('Email', 'N/A')}")
        print(f"     Phone: {contact_info.get('Phone', 'N/A')}")

    input("\nPress enter to return to the menu.")
    os.system('clear')


if __name__ == "__main__":

    while True:
            os.system('clear')
            print("\nContact Management System\n")
            print("1. Add Contact")
            print("2. Update Contact")
            print("3. Delete Contact")
            print("4. Display Contact")
            print("5. Display All Contacts")
            print("6. Exit")

            choice = input("\nEnter your choice (1-5): ")

            if choice == "1":
                os.system('clear')
                addContact()
            elif choice == "2":
                os.system('clear')
                updateContact()
            elif choice == "3":
                os.system('clear')
                deleteContact()
            elif choice == "4":
                os.system('clear')
                displayContact()
            elif choice == "5":
                os.system('clear')
                displayAllContacts()
            elif choice == "6":
                print("\nExiting the Contact Management System. Goodbye!")
                time.sleep(2)
                os.system('clear')
                break
            else:
                print("\nInvalid input. Please enter a number betweeen 1 and 5.")
                time.sleep(1.5)