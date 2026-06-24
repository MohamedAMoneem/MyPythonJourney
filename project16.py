import os
def clear():
    os.system("cls") if os.name =="nt" else os.system("clear")
contacts = {
}
def add():
    while True:
        id = input("insert contact id: ")
        if id.isdigit() == True:
            break
        else:
            clear()
            print("insert number only")
    name = input("insert contact name: ")
    while True:
        number = input("insert contact number: ")
        if number.isdigit() == True:
            break
        else:
            clear()
            print("insert number only")
    contacts[id] = {"name":name, "number":number}
def edit():
    while True:
        id = input("insert contact id: ")
        if id.isdigit() == True:
            break
        else:
            clear()
            print("insert number only")
    if id in contacts:
        name = input("insert new contact name: ")
        while True:
            number = input("insert new contact number: ")
            if number.isdigit() == True:
                break
            else:
                clear()
                print("insert number only")
        contacts[id] = {"name":name, "number":number}
    else:
        print("this id does not exist. . .")  
while True:
    clear()
    choice = int(input("""
    contact manager
                        
    1-add contact
    2-edit contact
    3-show contacts
    4-exit
                        
    """))
    if choice == 1:
        add()
    elif choice == 2:
        edit()
    elif choice == 3:
        clear()
        print(contacts)
        input("press enter to exit...")
    elif choice == 4:
        clear()
        break
    else:
        print("this choice does not exist")
