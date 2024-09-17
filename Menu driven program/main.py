dict1={}
count=0
while True:
    
    print("1.Registration\n2.Display\n3.Exit")
    choice=int(input("Enter your choice:"))

    if choice==1:
        n=int(input("Enter the number of people to register:"))
        
        for i in range(n):
            dict2={}
            dict2["Name"]=input("Enter Your Name:")
            dict2["Age"]=int(input("Enter Your Age:"))
            dict2["Place"]=input("Enter Your Place:")
            count+=1
            dict1[count]=dict2
            print()

    elif choice==2:
        if dict1:
            name=input("Enter the name you want to display:")
            found=False
            for key,value in dict1.items():
                if value["Name"]==name:
                    print(f"Member {key}: Name: {value['Name']}, Age: {value['Age']}, Place: {value['Place']}")
                    found=True
                    print()
                    break
            if not found:
                print("there are no registered members with this name")
        else:
            print("No Registered members")
            print()
    elif choice==3:
        print("Exiting from the program")
        break
    else:
        print("Invallid Choice...Please try again")

