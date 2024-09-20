def disarium(n):
    a=n
    length=len(str(a))
    sum=0
    while a>0:
        d=a%10
        sum=sum+ d**length
        a=a//10
        length-=1

    return sum

n=int(input("Enter a number:"))
result=disarium(n)

if result==n:
    print(f"{n} is a Disarium number")
else:
    print(f"{n} is not a Disarium number")