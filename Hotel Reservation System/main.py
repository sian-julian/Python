# def vallreservations(rooms):






def removeroom(rooms):
    roomno=input("Enter the Room number:")
    found=False

    for i,room in enumerate(rooms):
        if room['rnumber']==roomno:
            del rooms[i]
            found=True
            print("Room Deleted Successfully!!")
            break
    if found==True:
        print()
    else:
        print("Room not found!!")
        print()
        
            
def updateroom(rooms):
    print("**update room details**")
    roomno=input("Enter the Room number:")
    found=False

    for room in rooms:
        if room['rnumber']==roomno:
            room['rprice']=input("Enter the new price:")
            astatus="Available" if room['avstatus'] else "Not Available"
            room['avstatus']=astatus
            found=True
            print("Room Updated Successfully!!")
            break
    
    if found==True:
        print()
    else:
        print("Room not found!!")
        print()
                

def addroom(rooms):
    room={}
    while True:
        rnumber=input("Enter the room number:")
        if any(room['rnumber']==rnumber for room in rooms):
                print("Room Number already exists....try another Room number")
        else:
            room['rnumber']==rnumber
            break

    while True:
        rtype=input("Enter the type of room(single,double,suite):")

        if rtype=='single' or rtype=='double' or rtype=='suite' or rtype=='Single' or rtype=='Double' or rtype=='Suite':
             room['rtype']=rtype
             break
        else:
            print(f"SORRY WE DON'T HAVE {rtype} room in here...try another room")
            print()
    
    room['rprice']=int(input("Enter the room price:"))    
    # while True:
    #     rprice=int(input("Enter the Room price per night(Single-1000,Double-2000,Suite-3000):"))

    #     if rtype=='single' and rprice==1000:
    #         room['rprice']=rprice
    #         break
    #     elif rtype=='double' and rprice==2000:
    #         room['rprice']=rprice
    #         break
    #     elif rtype=='suite' and rprice==3000:
    #         room['rprice']=rprice
    #         break
    #     else:
    #         print("Invalid price for the selected room...try again")
    #         print()

    room['avstatus']=False
    print("Room Added Successfully!!")
    rooms.append(room)
    print()
    
    
def admin(admin_cred):
    print("**ADMIN PAGE**")
    admuser=input("Enter your Username:")
    adpass=input("Enter your Password:")
    print()

    for admin1 in admin_cred:
        if admin1['username']==admuser and admin1['password']==adpass:
            print("WELCOME SIAN")
            print()
            admin_menu()
        else:
            print("INVALID CREDENTIALS!!")
            print()


def admin_menu():
    while True:
        print("**ADMIN MENU**")
        print("1.Add Room\n2.Update Room Details\n3.Remove Room\n4.View All Reservations\n5.Generate Reports\n6.Exit from the Admin menu\n")
        print()
        ch=int(input("Enter your choice:"))

        if ch==1:
            addroom(rooms)
        elif ch==2:
            updateroom(rooms)
        elif ch==3:
            removeroom(rooms)
        # elif ch==4:
        #     vallreservations(rooms)
        # elif ch==5:
        #     genreport()
        elif ch==6:
            print("Exiting from the Admin Menu...")
            break
        else:
            print("INVALID CHOICE!!...Try again")
            print()

#receptionist section

def receptionist(reception_cred):
    print("**RECEPTION PAGE**")
    admuser=input("Enter your Username:")
    adpass=input("Enter your Password:")
    print()

    for reception1 in reception_cred:
        if reception1['username']==admuser and reception1['password']==adpass:
            print("WELCOME ANVITHA")
            print()
            reception_menu()
        else:
            print("INVALID CREDENTIALS!!")
            print()

def reception_menu():
    while True:
        print("**RECEPTION MENU**")
        print("1.Check-In Guest\n2.Check-Out Guest\n3.Make Reservation\n4.Cancel Reservation\n5.View Available Rooms:\n6.View Guest Details\n7.Exit from the Reception menu")
        print()
        ch=int(input("Enter your choice:"))

        if ch==1:
            checkin()
        # elif ch==2:
        #     checkout()
        # elif ch==3:
        #     mkreserve()
        # elif ch==4:
        #     canreserve()
        # elif ch==5:
        #     displayavrooms()
        # elif ch==6:
        #     displayguests()
        elif ch==7:
            print("Exiting from the Reception Menu...")
            break
        else:
            print("INVALID CHOICE!!...Try again")
            print()

def checkin():
    print()

    



    


rooms=[]
#admin credentials
admin_cred=[]
admin1={}
admin1['username']="sian"
admin1['password']="1234"
admin_cred.append(admin1)
#receptionist credentials
reception_cred=[]
reception1={}
reception1['username']="anvi"
reception1['password']="1234"

while True:
    print("***HOTEL RESERVATION SYSTEM***")
    print("1.Admin\n2.Receptionist\n3.Guest\n4.Exit\n")
    ch=int(input("Enter your choice:"))

    if ch==1:
        admin(admin_cred)
    elif ch==2:
        receptionist(reception_cred)
    # elif ch==3:
    #     guest()
    elif ch==4:
        print("Exiting from the program...")
        break
    else:
        print("INVALID CHOICE!!....Try again")
        print()

    
