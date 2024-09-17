members=[]
count=0

while True:
    print("1.Registration\n2.Display\n3.Exit")
    choice=int(input("Enter your choice:"))

    if choice==1:
        # n=int(input("Enter the number of people to register:"))
        users=[]

        # for i in users:
        name=input("Enter Your name:")
        age=int(input("Enter Your age:"))
        place=input("Enter your place:")
        
        users.append(name)
        users.append(age)
        users.append(place)

        members.append(users)
        print(members)
        print()

    elif choice==2:
        if members:
            name=input("Enter your name:")
            found=False

            for item in members:
                if item[0]==name:
                    print(f" Member {count+1}\n Name:{item[0]}\n Age:{item[1]}\n Place:{item[2]}")
                    found=True
                    print()
                    break
                count+=1
            # if found:
            #     break
            if not found:
                print("there are no members with this name")
        else:
            print("No Regeistered members")
        
    elif choice==3:
        print("Exiting from the program...")
        break
    else:
        print("Invalid choice.....Try again")
        print()


            
            
            
