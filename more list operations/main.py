list1=[12,14,16,18,20]
#l=list1 * 2
#print(l)

list2=[9,10,32,54,86]
#l=list1 + list2
#print(l)

a=len(list1)
b=len(list2)
#print(f"{a},{b}")
#print(a)
#print(b)

for i in list1:
    print(i)

print(31 in list2) #checks whether a no is present in a list or not

print(max(list1))
print(min(list1))

a=[1,2,3,4,5]
b=[3,4,5,6,7]
#intersection1=set(a).intersection(b)
intersection1=set(a) & set(b)
print(intersection1)
