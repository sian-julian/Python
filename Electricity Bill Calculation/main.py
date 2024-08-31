units=int(input("Enter the total units consumed:"))

if(units>0 and units <=100):
    total_bill=units*5
elif(units>100 and units<=200):
    total_bill=(100*5)+(units-100)*10
elif(units>200):  
    total_bill=(100*5)+(100*10)+(units-200)*15
else:
    print("Invalid bill")

print("Total Electricty Bill:",total_bill)
