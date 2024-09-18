a=int(input("Enter the number: "))
sum=0
r=0
while (a!=0):
    r=a%10
    sum=sum+r
    a=int(a/10)
print("Sum of digits:",sum)
