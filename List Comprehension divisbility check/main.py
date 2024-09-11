list1=[]

for i in range(1,51):
    list1.append(i)

print("Original List:",list1)

list2=[item for item in list1 if item % 3== 0 and item % 5== 0]
print()

print("List with Elements divisible by 3 and 5:",list2)