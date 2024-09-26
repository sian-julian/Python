class Additon:
    def add(self,a,b):
        print(f"Sum of {a}+{b}:",a+b)
        print()

class Subtraction:
    def sub(self,a,b):
        print(f"Difference of {a}-{b}:",a-b)
        print()

class Multiplication:
    def multiply(self,a,b):
        print(f"Difference of {a}*{b}:",a*b)
        print()
    
class Divide(Additon,Subtraction,Multiplication):
    def divide(self,a,b):
        if b<1:
            print("Division by zero or negative number is not possible")
            print()
        else:
            print(f"Difference of {a}/{b}:",a//b)
            print()

d=Divide()
while True:
    print("***MENU DRIVEN CALCULATOR***")
    print("1.Addition\n2.Differnce\n3.Product\n4.Division\n5.Exit")
    ch=int(input("Enter your choice:"))
    print()

    if ch==1:
        a=int(input("Enter the first number:"))
        b=int(input("Enter the second number:"))
        d.add(a,b)
    elif ch==2:
        a=int(input("Enter the first number:"))
        b=int(input("Enter the second number:"))
        d.sub(a,b)
    elif ch==3:
        a=int(input("Enter the first number:"))
        b=int(input("Enter the second number:"))
        d.multiply(a,b)
    elif ch==4:
        a=int(input("Enter the first number:"))
        b=int(input("Enter the second number:"))
        d.divide(a,b)
    elif ch==5:
        print("Exiting from the program....")
        break
    else:
        print("INVALID CHOICE!!....try again\n")








    
