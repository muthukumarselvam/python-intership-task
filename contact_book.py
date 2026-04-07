contacts = {}
while True:
    print("\n1. Add Contact  2. View All  3. Search  4. Exit")
    choice = input("Choose an option: ")
    if choice == '1':
        name = input("Enter Name: ")
        phone = input("Enter Phone: ")
        contacts[name] = phone
        print("Contact saved!")
    elif choice == '2':
        print("\n Contact List ")
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
    elif choice == '3':
        search = input("Enter Name to search: ")
        print(f"Phone: {contacts.get(search, 'Not Found')}")
    elif choice == '4':
        break