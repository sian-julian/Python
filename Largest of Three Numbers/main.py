a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))

if(a>b):
    if(a>c):
        print(f"{a} is the largest")
    else:
        print(f"{c} is the largest")
else:
    if(b>c):
        print(f"{b} is the largest")
    else:
        print(f"{c} is the largest")