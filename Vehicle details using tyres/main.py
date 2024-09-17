Tvehicles=[]
vehicle_no=0

while True:
    print("**Vehicle Management System***")
    print("1.Register\n2.Display\n3.Exit")
    ch=int(input("Enter your choice:"))

    if ch==1:
        vehicle_d=[]
        vehicle_no+=1
        owner=input("Enter Owner name:")
        vname=input("Enter Vehicle name:")
        vmodel=input("Enter vehicle model:")
        vehicle_d.append(vehicle_no)
        vehicle_d.append(owner)
        vehicle_d.append(vname)
        vehicle_d.append(vmodel)

        while True:
            ntyre=int(input("Enter number of tyres:"))
            if ntyre==2 or ntyre==3 or ntyre==4:
                vehicle_d.append(ntyre)
                Tvehicles.append(vehicle_d)
                print()
                break
            else:
                print(f"Sorry we do not accept {ntyre} tyre vehicles....please try again")

    elif ch==2:
        if Tvehicles:
            while True:
                print("1.2 tyres\n2.3 tyres\n3.4 tyres\n4.Exit from the Display menu")
                choice=int(input("Enter your choice:"))
                
                if choice in [1,2,3]:
                    tyre_d=choice+1
                    found=False

                    for vehicle in Tvehicles:
                        # for v in vehicle_d:
                        if vehicle[-1]==tyre_d:
                            print(f"Vehicle no: {vehicle[0]}\nVehicle Owner: {vehicle[1]}\nVehicle Name: {vehicle[2]}\nVehicle Model: {vehicle[3]}\nNumber of Tyres: {vehicle[4]}")
                            found=True
                            print()
                    if found:
                        print()
                        break
                    else:
                        print("No Vehicles Found!!\n")
                elif choice==4:
                    print("Exiting from this menu")
                    print()
                    break
        else:
            print("No Registered Vehicles!!")
            print()

    elif ch==3:
        print("Exiting from the program....")
        break
    else:
        print("Invalid choice.....Try Again")
        print()


            

           
            

