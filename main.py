from colorama import Fore
from cryptography.fernet import Fernet

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close
    return key

key = load_key()
fer = Fernet(key)

def view():
    website_chosen = input(Fore.WHITE + "What website password do you want? (MUST BE LOWERCASE) " + Fore.YELLOW)
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            website, user, passw = data.split("|")
            if website == website_chosen:
                print(Fore.RED + "Username: ", user)
                print(Fore.GREEN + "Password: ", fer.decrypt(passw.encode()).decode())
            else:
                continue

def add():
    website = input(Fore.WHITE + "Website Name (MUST BE LOWERCASE): " +  Fore.YELLOW)
    name = input(Fore.WHITE + "Account Name or Email: " + Fore.YELLOW)
    pwd = input("Account Password: " + Fore.YELLOW)

    with open('passwords.txt', 'a') as f:
        f.write(website + "|" + name + "|" + fer.encrypt(pwd.encode()).decode() + '\n')

while True:
    mode = input (Fore.WHITE + "Would you like to add a new password or view existing ones? VIEW, ADD. Press Q to quit. " + Fore.YELLOW)
    
    if mode == "q":
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid option.")
        continue