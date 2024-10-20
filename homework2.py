def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

def add_contact(args, contacts):
    if len(args) != 2:
        return "Please provide two arguments: name and phone number."
    
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    if len(args) != 2:
        return "Please provide two arguments: name and new phone number."
    
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return "Contact updated."
    return "Contact not found."

def show_phone(args, contacts):
    if len(args) != 1:
        return "Please provide the name of the contact."
    
    user_name = args[0]
    if user_name in contacts:
        return contacts[user_name]
    return "Contact not found."

def show_all(contacts):
    return contacts

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ").strip().lower()
        command, args = parse_input(user_input)

        match command:
            case "close" | "exit":
                print("Good bye!")
                break
            case "hello":
                print("How can I help you?")
            case "add":
                print(add_contact(args, contacts))
            case "change":
                print(change_contact(args, contacts))
            case "phone":
                print(show_phone(args, contacts))
            case "all":
                all_contacts = show_all(contacts)
                if all_contacts:
                    for name, phone in all_contacts.items():
                        print(f"{name}: {phone}")
                else:
                    print("No contacts found.")   
            case _:
                print("Invalid command.")

if __name__ == "__main__":
    main()