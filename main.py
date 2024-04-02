def contact_manager():
    contacts = {}
    condition = True
    while condition:
        message = 'choose one options below:\n1.add \n2.search\n3.menu\n4.exit'
        icon = input(message)

        if icon == "2":
            name = input("Enter your name:")
            print(contacts.get(name, f'{name} has not exist!'))
        elif icon == "1":
            name = input("Write name contact:")
            number = input("Enter number phon:")
            contacts[name] = number
        elif icon == "3":
            for contact in contacts:
                print(contact, contacts[contact])
        elif icon == "4":
            condition = False

contact_manager()
