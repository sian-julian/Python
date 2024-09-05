n=int(input("Enter a the size of the list:"))
a=[]
print("Items in the List")
for i in range(n):
    item=int(input())
    a.append(item)

print("The List:",a)

for i in range(n):
    for j in range(i+1,n):
        if a[i]>a[j]:
            temp=a[i]
            a[i]=a[j]
            a[j]=temp

print("Sorted List:",a)

