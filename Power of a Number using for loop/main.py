x=int(input("Enter a number:"))
y=int(input("Enter the power:"))

for i in range(y+1):
    if(i==y):
        power=x**y
        break
    
print("power:",power)

