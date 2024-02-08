contacts = {}
def add_cont():
    name = input("Enter contact name: ")
    num = input("Enter contact number: ")
    contacts[name] = num
    print(f"{name} added to contacts.")

def search_cont():
    name = input("Enter contact name to search: ")
    if name in contacts:
        print(f"{name}: {contacts[name]}")
    else:
        print(f"{name} not found in contacts.")

def display_conts():
    if contacts:
        print("Contacts:")
        for name, num in contacts.items():
            print(f"{name}: {num}")
    else:
        print("No contacts in the list.")

def delete_cont():
    name = input("Enter contact name to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"{name} deleted from contacts.")
    else:
        print(f"{name} not found in contacts.")

def contbk():
    while True:
        print("\nContact Book")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Display Contacts")
        print("4. Delete Contact")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            add_cont()
        elif choice == '2':
            search_cont()
        elif choice == '3':
            display_conts()
        elif choice == '4':
            delete_cont()
        elif choice == '5':
            print("Exiting Contact Book.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    contbk()
