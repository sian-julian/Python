a=[]
n=int(input("Enter the size of the list:"))

for i in range(n):
    item=int(input())
    a.append(item)

print(a)

unique=sorted(p for p in a if a.count(p)==1)
if not unique:
    print("all Elements are duplicates")
else:
    print(unique)
    print("Largest element in the list:",unique[-1])


           


