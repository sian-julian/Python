list1=[]
dict1={}
n=int(input("Enter the number of students you want to enter:"))

for i in range(n):
    dict1={}
    dict1["id"]=i+1
    dict1["Name"]=input("Enter the student's Name:")
    dict1["Age"]=int(input("Enter the Student's Age:"))
    if(dict1["Age"]<=0):
        dict1["Age"]=int(input("Inavlid Age....Enter the Age again:"))
    dict1["Maths"]=input("Enter the Student's marks in Maths:")
    dict1["Physics"]=input("Enter the Student's marks in Physics:")
    dict1["Chemistry"]=input("Enter the Student's marks in Chemistry:") 
    list1.append(dict1)
    print()

print(list1)
