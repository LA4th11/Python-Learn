# Function to add a new contact to the phonebook
def add_contacts(phonebook):
    name = input("Contact name: ")  # Prompt user for contact name
    
    # Check if the contact name already exists in the phonebook
    if name in phonebook:
        print("Contact name already exists!")  # Notify if the contact is a duplicate
    else:
        # If the name is new, prompt user for phone number and email
        phone_number = input("Contact number: ")
        email = input("Email address: ")
        
        # Add new contact details to the phonebook dictionary
        phonebook[name] = {
            'Phone_Number': phone_number,
            'Email': email
        }
        print("Successfully Added!")  # Confirm contact was added

# Function to search for a contact in the phonebook
def search_contact(phonebook):
    name = input("Name to search: ")  # Prompt user for the contact name to search
    
    # Check if the contact exists
    if name in phonebook:
        # Display the contact details if found
        print(f"Name: {name}")
        print(f"Phone number: {phonebook[name]['Phone_Number']}")
        print(f"Email: {phonebook[name]['Email']}")
    else:
        # Notify user if contact is not found
        print("Contact person does not exist!")

# Function to update an existing contact's details
def update_contact(phonebook):
    name = input("Name to search: ")  # Prompt user for the contact name to update
    
    # Check if the contact exists in the phonebook
    if name in phonebook:
        # Prompt user for new phone number and email
        phone_update = input(f"Update phone number for {name}: ")
        email_update = input(f"Update email for {name}: ")
        
        # Update the contact's details
        phonebook[name] = {
            'Phone_Number': phone_update,
            'Email': email_update
        }
        print("Update Successful!")  # Confirm the update was successful
    else:
        # Notify user if contact is not found
        print("Contact person does not exist!")

# Function to display all contacts in the phonebook
def show_contacts(phonebook):
    # Loop through each contact in the phonebook
    for key, obj in phonebook.items():
        print(key)  # Print contact name
        
        # Loop through the contact details (phone number and email)
        for objs in obj:
            print(f"{objs}: {obj[objs]}")  # Print each detail

# Main function to handle user interaction and menu
def main():
    # Initialize phonebook with one contact
    phonebook = {
        'Enzo': {
            'Phone_Number': '09668759370',
            'Email': 'Enzo@example.com'
        }
    }
    
    # Menu options mapped to corresponding functions
    functions_menu = {
        '1': add_contacts,
        '2': search_contact,
        '3': update_contact,
        '4': show_contacts
    }
    
    # Infinite loop to keep showing the menu until the user decides to exit
    while True:
        # Display menu options
        print("\nMenu Select:")
        print("1. Add Contact\n2. Search Contact\n3. Update Contact\n4. Show Contacts\n5. Exit")
        
        user_input = input("Enter your choice: ")  # Get user input for menu option
        
        # Execute corresponding function based on user input
        if user_input in functions_menu:
            functions_menu[user_input](phonebook)
        elif user_input == '5':  # Exit the program
            break
        else:
            print("Invalid Input!")  # Handle invalid menu selection

# Entry point of the program
if __name__ == "__main__":
    main()
