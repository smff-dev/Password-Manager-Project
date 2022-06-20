master_pwd = input ("What is the master password? ")

def view():
    pass

def add():
    name = input("Account Name or Email: ")
    pwd = input("Account Password: ")

    with open('passwords.txt', 'a') as f:
        pass


while True:
    mode = input ("Would you like to add a new password or view existing ones? VIEW, ADD. Press Q to quit. " ).lower
    
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid option.")
        continue