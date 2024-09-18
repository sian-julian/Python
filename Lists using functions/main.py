def even(list1):
    t1=tuple(item for item in list1 if item%2==0)
    print("Even numbers in the tuple:",t1)
def odd(list1):
    t1=tuple(item for item in list1 if item%2!=0)
    print("Odd numbers in the tuple:",t1) 

list1=[]
n=int(input("Enter the size of the list:"))

for i in range(n):
    item=int(input())
    list1.append(item)

even(list1)
odd(list1)