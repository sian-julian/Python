def sum_list(lis,n):
    if n<0:
        return 0
    else:
        return (lis[n]+sum_list(lis,n-1))
lis=[]
n=int(input("Enter the number of elements: "))
print("Enter the elements:")
for i in range(n):
    a=int(input())
    lis.append(a)
print("Sum of digits is:",sum_list(lis,n-1))