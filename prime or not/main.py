n=int(input("Enter a number:"))
isprime=False

if n<=1:
    isprime=False
else:
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            isprime=False
            break
        else:
            isprime=True
            
if isprime:
    print(f"{n} is a prime number")
else:
    print(f"{n} is not a prime number")

