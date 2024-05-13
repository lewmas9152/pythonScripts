from cryptography.fernet import Fernet
"""def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
        print(key)"""


def load_key():
    file= open("key.key", "rb")
    key = file.read()
    file.close()
    return key

master_pwd = input("Please enter your master password: ")

key = load_key()  + master_pwd.encode()
fer = Fernet(key) 

def view() :
    with open("passwords.txt", "r") as f :
        for line in f.readlines():
            data = line.rstrip()
            name, passw = data.split("|")
            print("Account:", name, "| Password:", fer.decrypt(passw.encode()).decode())
            

def add() : 
    with open("passwords.txt","a") as f:
        accName = input("Enter account Name: ")
        pwd = input("Enter password: ")

        f.write(accName+ "|" +fer.encrypt(pwd.encode()).decode() +"\n")




while True :
    mode = input("Do you want to add a password or view your passwords?(add/view, q if you want to quit) ").lower()

    if mode == "q" :
        print("Goodbye👋")
        break

    elif mode == "add" :
        add()

    elif mode == "view" :
        view()

    else:
        print("Invalid option!!")
        continue



   