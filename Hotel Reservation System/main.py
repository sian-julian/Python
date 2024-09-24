#Guest Section

def guest(Guests):
    while True:
        print("**GUEST PAGE**\n")
        print("1.Register\n2.Login\n3.Exit from guest page")
        print()
        ch=int(input("Enter your choice:"))

        if ch==1:
            register(Guests)
        elif ch==2:
            login(Guests)
        elif ch==3:
            print("Exiting from the Guest page...")
            break
        else:
            print("INVALID CHOICE!!...Try again")
            print()


def register(Guests):
    print("**Guest Registration Page**\n")
    Guest={}

    Guest['gname']=input("Enter your Name:")
    while True:
        gphone=int(input("Enter your Phone Number:"))
        if any(Guest['gphone']==gphone for Guest in Guests):
            print("Phone Already exists....try Another phone Number")
            print()
        else:
            Guest['gphone']=gphone
            break

    Guest['gaddress']=input("Enter your address:")

    while True:
        uname=input("Enter a Username:")

        if any(Guest['uname']==uname for Guest in Guests):
            print("Username already exists...Try another Username")
            print()
        else:
            Guest['uname']=uname
            break

    Guest['gpass']=input("Enter a password:")
    Guest['guestid'] = str(len(Guests)+1)
    print(f"Guest {Guest['gname']} is assingned with the Guest id: {Guest['guestid']}\n")
    Guests.append(Guest)
    print("Guest Registration Successfull!!")


def login(Guests):
    print("**Guest Login Page**\n")
    guname=input("Enter your Username:")
    gpass=input("Enter your Password:")

    for Guest in Guests:
        if Guest['uname']==guname and Guest['gpass']==gpass:
            print("WELCOME")
            print()
            guest_menu(Guests)
        else:
            print("INVALID CREDENTIALS!!")
            print()
            break


def guest_menu(Guests):
    while True:
        print("**Guest Menu**\n")
        print("1.View Available Rooms\n2.Make a Reservation\n3.View Reservation Status:\n4.Update Personal Information\n5.Cancel Reservation\n6.Exit from the Guest menu\n")
        print()
        ch=int(input("Enter your choice:"))

        if ch==1:
            viewavroom(rooms)
        elif ch==2:
            mkreserve2(Guests,rooms)        #Make a Reservation
        elif ch==3:
            vrstatus(Guests,rooms)          #View Reservation Status
        elif ch==4:
            updatepsnlinfo(Guests)
        elif ch==5:
            canreserve2(Guests,rooms)        #cancel reservation
        elif ch==6:
            print("Exiting from the Guest Menu....")
            break
        else:
            print("INVALID CHOICE!!...try again")
            print()


def viewavroom(rooms):
    print("**Available Rooms**\n")

    for i,room in enumerate(rooms,start=1):
        if room['avstatus']=="Available":
            print(f"sl no: {i}")
            print(f"Room Number: {room['rnumber']}\nRoom Type: {room['rtype']}\nRoom Price: {room['rprice']}")
            print()
        else:
            print("No Rooms Available!!")
            print()
            break

def mkreserve2(Guests,rooms):
    print("**Guest-Make Reservation**\n")
    gusername=input("Enter your Username:")

    for Guest in Guests:
        if Guest['uname']==gusername:
            roomno=input("Enter the room number:")

            for room in rooms:
                if room['rnumber']==roomno and room['avstatus']==True:
                    check_in=input("Enter the Check in Date(dd/mm/yyyy):")
                    check_out=input("nter the Check out Date(dd/mm/yyyy):")
                    room['avstatus']="Reserved"     #room unavailabe now since it is Reserved
                    Guest['reservation']={'room':roomno,'check_in':check_in,'check_out':check_out}
                    print("Rservation Successfull!!")
                    print()
                    break  
                else:
                    print("Room is unavailable or doesn't exist")
                    print()
                    break
        else:
            print("Invalid Username!!")
            print()
            break


def vrstatus(Guests,rooms):
    print("**Reservation Status**\n")

    for Guest in Guests:
        print(f"Guest id: {Guest['guestid']}")
        print(f"Guest Name: {Guest['gname']}")
        print(f"Guest room: {Guest['reservation']['room']}")
        print(f"Guest check in date: {Guest['reservation']['check_in']}")
        print(f"Guest check out date: {Guest['reservation']['check_out']}")
        gmatch=Guest['reservation']['room']
        for room in rooms:
            if room['rnumber']==gmatch:
                print(f"Current Reservation Status: {room['avstatus']}")
                print()
      
                        
def updatepsnlinfo(Guests):
    print("**Update Personal Information**\n")

    guest_phno=input("Enter Guest Id:")
    found=False
    for Guest in Guests:
        if Guest['gphone']==guest_phno:
            Guest['gphone']=input("Enter new phone:")
            Guest['gaddress']=input("Enter new Address:")
            print("Information Updated Successfully!!")
            found=True
            break
    if found:
        print()
    else:
        print("Guest Not Found!!")
        print()


def canreserve2(Guests,rooms):
    print("**Cancel Reservation**\n")
    guest_id=input("Enter Guest Id:")
    room_no=input("Enter the room number:")

    for Guest in Guests:
        if Guest['guestid']==guest_id and Guest['reservation']['room']==room_no:
            del Guest['reservation']
            for room in rooms:
                if room['avstatus']=="Reserved":
                    room['avstatus']="Available"
                    print("Reservation Cancelled Successfully!!")
                    print("Reservation Status Updated!!")
                    print()
                    break
        else:
            print("No reservation found for this guest")
            print()


#Admin Section

def genreport(rooms):
    print("**Hotel Report**\n")

    totalrooms=len(rooms)
    print(f"Total number of rooms: {totalrooms}")

    availablerooms=[room for room in rooms if room['avstatus']=="Available"]
    print(f"Available Rooms: {len(availablerooms)}")
    
    reservedrooms=[room for room in rooms if room['avstatus']=="Reserved"]
    print(f"Reserved Rooms: {len(reservedrooms)}")

    totalrevenue=0
    for room in rooms:
        if room['avstatus']=="Reserved":
            totalrevenue +=room['rprice']
    
    print(f"Total Revenue Generated: {totalrevenue}")
        
    occupancy_rate=0

    if totalrooms>0:
        occupancy_rate=(reservedrooms/totalrooms)*100
    else:
        occupancy_rate=0
    
    print(f"Occupancy Rate: {occupancy_rate}")
    print()

def vallreservations(Guests,rooms):
    print("**View All Reservations**\n")
    found=False
    for Guest in Guests:
        if 'reservation' in Guest:
            print(f"Guest: {Guest['gname']}")
            print(f"Guest Address: {Guest['gaddress']}")
            print(f"Room: {Guest['reservation']['room']}")
            print(f"Check-in: {Guest['reservation']['check_in']}")
            print(f"Check-out: {Guest['reservation']['check_out']}")
            found=True
            print()
    
    if not found:
        print("There are no reservations!!")
        print()
    
    
def removeroom(rooms):
    print("**Remove Rooms**\n")
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
    print("**update room details**\n")
    roomno=input("Enter the Room number:")
    found=False

    for room in rooms:
        if room['rnumber']==roomno:
            room['rprice']=input("Enter the new price:")
            astatus="Available" if room['avstatus'] else "Reserved"
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
    print("**Add Rooms**\n")
    room={}
    while True:
        rnumber=input("Enter the room number:")
        if any(room['rnumber']==rnumber for room in rooms):
                print("Room Number already exists....try another Room number")
        else:
            room['rnumber']=rnumber
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

    room['avstatus']="Available"       #Available
    print("Room Added Successfully!!")
    rooms.append(room)
    print()
    
    
def admin(admin_cred):
    print("**ADMIN PAGE**\n")
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
        print("**ADMIN MENU**\n")
        print("1.Add Room\n2.Update Room Details\n3.Remove Room\n4.View All Reservations\n5.Generate Reports\n6.Exit from the Admin menu\n")
        print()
        ch=int(input("Enter your choice:"))

        if ch==1:
            addroom(rooms)
        elif ch==2:
            updateroom(rooms)
        elif ch==3:
            removeroom(rooms)
        elif ch==4:
            vallreservations(Guests,rooms)
        elif ch==5:
            genreport(rooms)
        elif ch==6:
            print("Exiting from the Admin Menu...")
            break
        else:
            print("INVALID CHOICE!!...Try again")
            print()

#receptionist section

def receptionist(reception_cred):
    print("**RECEPTION PAGE**\n")
    admuser=input("Enter your Username:")
    adpass=input("Enter your Password:")
    print()

    for reception1 in reception_cred:
        if reception1['username']==admuser and reception1['password']==adpass:
            print("WELCOME ANVITHA")
            print()
            reception_menu()
            break
        else:
            print("INVALID CREDENTIALS!!")
            print()
    
           

def reception_menu():
    while True:
        print("**RECEPTION MENU**\n")
        print("1.Check-In Guest\n2.Check-Out Guest\n3.Make Reservation\n4.Cancel Reservation\n5.View Available Rooms:\n6.View Guest Details\n7.Exit from the Reception menu")
        print()
        ch=int(input("Enter your choice:"))

        if ch==1:
            checkin(Guests,rooms)
        elif ch==2:
            checkout(Guests,rooms)
        elif ch==3:
            mkreserve1(Guests,rooms)
        elif ch==4:
            canreserve1(Guests,rooms)
        elif ch==5:
            displayavrooms(rooms)
        elif ch==6:
            displayguests(Guests)
        elif ch==7:
            print("Exiting from the Reception Menu...")
            break
        else:
            print("INVALID CHOICE!!...Try again")
            print()

def checkin(Guests,rooms):
    print("**Check In Guest**\n")
    guest_id=input("Enter Guest Id:")
    room_no=input("Enter the room number:")
    checkin=input("Enter the check in date(dd/mm/yyy):")

    for Guest in Guests:
        if Guest['guestid']==guest_id and Guest['reservation']['room']==room_no and Guest['reservation']['check_in']==checkin:
            for room in rooms:
                if room['avstatus']=="Reserved":
                    room['avstatus']="Occupied"
                    print("Room Availability status Updated!! Guest checked in")
                    print(f"Guest {Guest['gname']} checked into room {room_no}.")
                    print()
                    break
        else:
            print("No reservation found for this guest")
            print()
            break

def checkout(Guests,rooms):
    print("**Check Out Guest**\n")
    guest_id=input("Enter Guest Id:")
    room_no=input("Enter the room number:")

    for Guest in Guests:
        if Guest['guestid']==guest_id and Guest['reservation']['room']==room_no:
            for room in rooms:
                if room['avstatus']=="Ocuupied":
                    room['avstatus']="Available"
                    print("Room Availability status Updated!! Guest checked Out")
                    print(f"Guest {Guest['gname']} checked out from the room {room_no}.")
                    print()
                    break
        else:
            print("No reservation found for this guest")
            print()
            break

            
def mkreserve1(Guests,rooms):
    print("**Receptionist-Make Reservation**\n")
    Guest={}
    Guest['gname']=input("Enter Guest Name:")
    while True:
        gphone=int(input("Enter Guest Phone Number:"))
        if any(Guest['gphone']==gphone for Guest in Guests):
            print("Phone Already exists....try Another phone Number")
            print()
        else:
            Guest['gphone']=gphone
            break

    Guest['gaddress']=input("Enter your address:")

    while True:
        uname=input("Enter a Username:")

        if any(Guest['uname']==uname for Guest in Guests):
            print("Username already exists...Try another Username")
            print()
        else:
            Guest['uname']=uname
            break

    Guest['gpass']=input("Enter a password:")
    Guest['guestid'] = str(len(Guests)+1)
    print(f"Guest {Guest['gname']} is assingned with the Guest id: {Guest['guestid']}\n")
    # Guests.append(Guest)
    # print("Guest Registration Successfull!!")

    for room in rooms:
        roomno=input("Enter the room number:")
        if room['rnumber']==roomno and room['avstatus']=="Available":
            check_in=input("Enter the Check in Date(dd/mm/yyyy):")
            check_out=input("Enter the Check out Date(dd/mm/yyyy):")
            room['avstatus']="Reserved"     #room unavailabe now since reserved
            Guest['reservation']={'room':roomno,'check_in':check_in,'check_out':check_out}
            print("Rservation Successfull!!")
            print()
            break  
        else:
            print("Room is unavailable....try another room!!")
            print()
            
    
    Guests.append(Guest)
    print("Guest Registration and Room Reservation Successfull!!")
    print()


def canreserve1(Guests,rooms):
    print("**Cancel Reservation**\n")
    guest_id=input("Enter Guest Id:")
    room_no=input("Enter the room number:")

    for Guest in Guests:
        if Guest['guestid']==guest_id and Guest['reservation']['room']==room_no:
            del Guest['reservation']
            for room in rooms:
                if room['avstatus']=="Reserved":
                    room['avstatus']="Available"
                    print("Reservation Cancelled Successfully!!")
                    print("Reservation Status Updated!!")
                    print()
                    break
        else:
            print("No reservation found for this guest")
            print()



def displayavrooms(rooms):
    print("**All Available Rooms**\n")
    if rooms:
        for i,room in enumerate(rooms,start=1):
            if room['avstatus']=="Available":
                print(f"Room: {i}")
                print(f"Room Number: {room['rnumber']}")   
                print(f"Room Type: {room['rtype']}")
                print(f"Room Price: {room['rprice']}")  
                print()
    else:
        print("No rooms Available!!")
        print()


def displayguests(Guests):
    print("**All Existing Guests**\n")
    if Guests:
        for i,Guest in enumerate(Guests,start=1):
            print(f"sl no: {i}")
            print(f"Guest Name: {Guest['gname']}")
            print(f"Guest Phone Number: {Guest['gphone']}")
            print(f"Guest Address: {Guest['gaddress']}")
            print(f"Guest id: {Guest['guestid']}")
            print(f"Guest Rerservation Status: {Guest['reservation']}")
            print()
    else:
        print("No Existing Guests:")
        print()


#Main Section
rooms=[]
Guests=[]
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
reception_cred.append(reception1)

while True:
    print("***HOTEL RESERVATION SYSTEM***\n")
    print("1.Admin\n2.Receptionist\n3.Guest\n4.Exit\n")
    ch=int(input("Enter your choice:"))

    if ch==1:
        admin(admin_cred)
    elif ch==2:
        receptionist(reception_cred)
    elif ch==3:
        guest(Guests)
    elif ch==4:
        print("Exiting from the program...")
        break
    else:
        print("INVALID CHOICE!!....Try again")
        print()

    
