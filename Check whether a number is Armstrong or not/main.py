a=int(input("Enter a number:"))
c=a
b=str(a)
length=len(b)
print(length)
print(a)
sum=0
while c>0:
    d=c%10
    sum=sum + d**length
    c=c//10

if(sum==a):
    print(f"{a} is Armstrong")
else:
    print(f"{a} is not Armstrong")
