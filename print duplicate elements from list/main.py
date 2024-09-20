list1=[]
n=int(input("Enter the size of the list:"))

for i in range(n):
    item=int(input())
    list1.append(item)

print("original list:",list1)
# count=0
list2=[]
for item in list1:
    if item not in list2:
        list2.append(item)

print(list2)