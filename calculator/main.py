print("1.add\n2.Subtract\n3.Multiply\n4.Divide")
ch=int(input("Enter your choice:"))
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))

if(ch==1):
    print(f"{a}+{b}:",a+b)
elif(ch==2):
    print(f"{a}-{b}:",a-b)
elif(ch==3):
    print(f"{a}*{b}:",a*b)
elif(ch==4):
    print(f"{a}/{b}:",float(a+b))
else:
    print("invalid choice")

