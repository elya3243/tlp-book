def contact_manager():
    contacts = {}
    condition = True
    while condition:
        icon = input("search, menu or add?")
        if icon == "search":
            name = input("Enter your name:")
            print(contacts.get(name, f'{name} has not exist!'))
        if icon == "add":
            name = input("Write name contact:")
            number = input("Enter number phon:")
            contacts[name] = number
        if icon == "menu":
            for contact in contacts:
                print(contact, contacts[contact])
        if icon == "exit":
            condition = False

contact_manager()
