def armstrong(n):
    a=n
    b=n
    sum=0
    length=len(str(a))

    while b>0:
        d=b%10
        sum=sum+d**length
        b=b//10
    return sum
    

n=int(input("Enter a number:"))
sum=armstrong(n)

if sum==n:
    print(f"{n} is an Armstrong number")
else:
    print(f"{n} is not an Armstrong number")