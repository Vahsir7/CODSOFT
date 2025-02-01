class Contact:
    '''
    This class represents a contact in the contact book.
    Each contact has a name, phone number, email, and address.
    '''
    def __init__(self, name, phone, email, address):
        self.__name = name
        self.__phone = phone
        self.__email = email
        self.__address = address
    
    def get_name(self):
        return self.__name
    
    def get_phone(self):
        return self.__phone
    
    def get_email(self):
        return self.__email
    
    def get_address(self):
        return self.__address
    
    def set_name(self, name):
        self.__name = name
    
    def set_phone(self, phone):
        self.__phone = phone
    
    def set_email(self, email):
        self.__email = email
    
    def set_address(self, address):
        self.__address = address

def display(contacts):
    if not contacts:
        print("No contacts available.")
        return False

    max_id_width = len("id")
    max_name_width = len("Name")
    max_phone_width = len("Phone")
    max_email_width = len("Email")
    max_address_width = len("Address")
    
    for i, contact in enumerate(contacts, start=1):
        max_id_width = max(max_id_width, len(str(i)))
        max_name_width = max(max_name_width, len(contact.get_name()))
        max_phone_width = max(max_phone_width, len(contact.get_phone()))
        max_email_width = max(max_email_width, len(contact.get_email()))
        max_address_width = max(max_address_width, len(contact.get_address()))
    
    padding = 4
    max_id_width += padding
    max_name_width += padding
    max_phone_width += padding
    max_email_width += padding
    max_address_width += padding
    
    header = f"{'id':<{max_id_width}}| {'Name':<{max_name_width}}| {'Phone':<{max_phone_width}}| {'Email':<{max_email_width}}| {'Address':<{max_address_width}}"
    print(header)
    
    separator = "-" * len(header)
    print(separator)
    
    for i, contact in enumerate(contacts, start=1):
        row = f"{i:<{max_id_width}}| {contact.get_name():<{max_name_width}}| {contact.get_phone():<{max_phone_width}}| {contact.get_email():<{max_email_width}}| {contact.get_address():<{max_address_width}}"
        print(row)

def search_contact(contacts, search_term):
    found = False
    for contact in contacts:
        if search_term in contact.get_name() or search_term in contact.get_phone():
            print(f"Found Contact: {contact.get_name()}\nPhone: {contact.get_phone()}\nEmail: {contact.get_email()}\nAddress: {contact.get_address()}")
            found = True
    if not found:
        print("No contact found.")


contacts = []
while True:
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    choice = input("Enter your choice: ")
    
    if choice == '1':
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        address = input("Enter address: ")
        contacts.append(Contact(name, phone, email, address))
        print("Contact added successfully.")
    elif choice == '2':
        display(contacts)
    elif choice == '3':
        search_term = input("Enter name or phone number to search: ")
        search_contact(contacts, search_term)
    elif choice == '4':
        display(contacts)
        try:
            index = int(input("Enter the contact number to update: ")) - 1
            if 0 <= index < len(contacts):
                contact = contacts[index]
                print("1. Update Name\n2. Update Phone\n3. Update Email\n4. Update Address")
                update_choice = input("Enter your choice: ")
                if update_choice == '1':
                    contact.set_name(input("Enter new name: "))
                elif update_choice == '2':
                    contact.set_phone(input("Enter new phone: "))
                elif update_choice == '3':
                    contact.set_email(input("Enter new email: "))
                elif update_choice == '4':
                    contact.set_address(input("Enter new address: "))
                else:
                    print("Invalid choice.")
                print("Contact updated successfully.")
            else:
                print("Invalid contact number.")
        except ValueError:
            print("Invalid input.")
    elif choice == '5':
        display(contacts)
        try:
            index = int(input("Enter the contact number to delete: ")) - 1
            if 0 <= index < len(contacts):
                contacts.pop(index)
                print("Contact deleted successfully.")
            else:
                print("Invalid contact number.")
        except ValueError:
            print("Invalid input.")
    elif choice == '6':
        print("Exiting Contact Book. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

