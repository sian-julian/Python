dict1={}
count=0

while True:
    print("1.Register\n2.Login\n3.Exit")
    ch=int(input("Enter your choice:"))

    if ch==1:
        while True:
            print("***REGISTRATION PAGE***")
            username=input("Enter a Username:")
            if any(user["username"]==username for user in dict1.values()):
                print("This Username already exists....Please try another one.")
            else:
                dict2={}
                dict2["username"]=username
                dict2["password"]=input("Enter a password:")
                dict2["Name"]=input("Enter your Name:")
                dict2["Age"]=int(input("Enter your Age:"))
                dict2["place"]=input("Enter your place:")
                count+=1
                dict1[count]=dict2
                print(dict1)
                break
    
    elif ch==2:
        print("***LOGIN PAGE***")
        if dict1:
            while True:
                username=input("Enter Your Username:")
                password=input("Enter your password:")

                # while True:
                found=False
                for key,value in dict1.items():
                    if value["username"]==username and value["password"]==password:
                        print()
                        print("Login Successfully!!")
                        print(f"Id: {key}\nName: {value["Name"]}\nAge: {value["Age"]}\nPlace: {value["place"]}")
                        found=True
                        print()
                        break
                if found:
                    break
                if not found:
                    print("Invalid Credentials or Account Does not Exist....Please Try again")
        else:
            print("No Registered members")
            print()

    elif ch==3:
        print("Exiting from the Program.....")
        break
    
    else:
        print("Invalid Choice.....Try again")
        



            
            
            
          
        
            
            