a=[]
n=int(input("Enter the size of the list:"))

for i in range(n):
    item=int(input())
    a.append(item)

print("The list:",a)

dict1={}

for item in a:
    if item in dict1:
        dict1[item]+=1
    else:
        dict1[item]=1

print(dict1)    

