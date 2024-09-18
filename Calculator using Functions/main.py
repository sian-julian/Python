def add(a,b):
    c=a+b
    print(f"sum of {a}+{b}:",c)
    print()
def sub(a,b):
    c=a-b
    print(f"Difference of {a}-{b}:",c)
    print()
def multiply(a,b):
    c=a*b
    print(f"Product of {a}*{b}:",c)
    print()
def divide(a,b):
    if b<1:
        print("Division by zero or negative number is not possible")
        print()
    else:
        c=a/b
        print(f"result of {a}/{b}:",c)
        print()


while True:
    print("***Calculator***")
    print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Exit")
    ch=int(input("Enter your choice:"))
    
    if ch==1:
        a=int(input("Enter the first number:"))
        b=int(input("Enter the second number:"))
        add(a,b)
    elif ch==2:
        a=int(input("Enter the first number:"))
        b=int(input("Enter the second number:"))
        sub(a,b)
    elif ch==3:
        a=int(input("Enter the first number:"))
        b=int(input("Enter the second number:"))
        multiply(a,b)
    elif ch==4:
        a=int(input("Enter the first number:"))
        b=int(input("Enter the second number:"))
        divide(a,b)
    elif ch==5:
        print("Exiting from the program...")
        break
    else:
        print("INVALID CHOICE....try again")
        print()
    

    