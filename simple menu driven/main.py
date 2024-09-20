def login(users):
    username=input("Enter your username:")
    password=input("Enter your password:")

    for user in users:
        if user['unam']==username and user['pass']==password:
            print("Login successfull!!")
            print("WELCOME")
            print()
            break
        else:
            print("INVALID CREDENTIALS!!")
            print()


def register(users):
    user={}

    user['name']=input("Enter your name:")
    user['age']=int(input("Enter your age:"))
    user['address']=input("Enter your address:")

    while True:
        username=input("Enter your Username:")

        if any(user['unam']==username for user in users):
            print("Username already exists...try another Username")
            print()
        else:
            user['unam']=username
            break 

    user['pass']=input("Enter a password:")
    users.append(user)
    print("registration Successfull!!")
    print()


users=[]

while True:
    print("***MENU DRIVEN***")
    print("1.register\n2.login\n3.Exit")
    ch=int(input("Enter your choice:"))

    if ch==1:
        register(users)
    elif ch==2:
        login(users)
    elif ch==3:
        print("Exiting from the program....")
        break
    else:
        print("INVALID CHOICE!!")
        print()