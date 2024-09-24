def missno(a):
    print()
    right=a[0]

    # for i in a:
    #     if i>right:
    #         right=i

    # print(right)
    left=a[-1]
    
    # for i in a:
    #     if i<left:
    #         left=i
            
    # print(left)
    
    list1=[]

    for item in range(1,left):
        if item not in a:
            list1.append(item)

    print(list1[0])


a=[]
n=int(input("Enter the size of the list:"))

for item in range(n):
    item=int(input())
    a.append(item)
print("original list:",a)
missno(a)