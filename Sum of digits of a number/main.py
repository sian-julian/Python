n=int(input("Enter a number:"))
temp=n
sum=0

while n>0:
    d=n%10
    sum=sum+d
    n=n//10

print(f"Sum of Digits of {temp} is:",sum)