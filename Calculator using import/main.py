from Calculatorfn import calculatorfn

print("**Calculator**")
print("1.Addition\n2.Differnce\n3.Product\n4.Division")
ch=int(input("Enter your choice:"))
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))

if ch==1:
    calculatorfn.add(a,b)
elif ch==2:
    calculatorfn.sub(a,b)
elif ch==3:
    calculatorfn.multiply(a,b)
elif ch==4:
    calculatorfn.divide(a,b)
else:
    print("INVALID CHOICE!!")

