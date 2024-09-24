lis=[]
l=[]
def remove_elements():
    for i in lis:
        if i>=0:
            l.append(i)
    # print(l)
def missing_no():
    a=1
    for i in l:
        if i==a:
            a+=1
    print("The missing number is:",a)
        

n=int(input("Enter the number of elements: "))
print("Enter the elements: ")
for i in range(n):
    a=int(input())
    lis.append(a)
lis=sorted(lis)
# print(lis)
remove_elements()
missing_no()