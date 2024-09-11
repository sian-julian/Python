n=int(input("Enter a number:"))
list1=[[0 for x in range(n)] for y in range(n)]

num=1
low=0
high=n-1     
count=int((n+1)/2)

for i in range(count):
    for j in range(low,high+1):
        list1[low][j]=num
        num=num+1
    for j in range(low+1,high+1):
        list1[j][high]=num
        num=num+1
    for j in range(high-1,low-1,-1):
        list1[high][j]=num
        num=num+1
    for j in range(high-1,low,-1):
        list1[j][low]=num
        num=num+1
    low=low+1
    high=high-1

for i in range(n):
    for j in range(n):
        print(list1[i][j],end='\t')
    print()
