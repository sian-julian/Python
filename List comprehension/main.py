list1=[]
n=int(input("Enter the size of the list:"))

for i in range(n):
    item=input()
    list1.append(item)

print("Original list:",list1)

list2=[x[0] for x in list1]
print("First character in each item:",list2)
