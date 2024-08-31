dict1={}
n=int(input("Enter the number of people u want to save the information to:"))

for i in range(n):
    dict2={}
    dict2["Name"]=input("Enter your name:")
    dict2["Age"]=int(input("Enter your age:"))
    dict2["Salary"]=float(input("Enter your salary:"))
    dict2["City"]=input("Enter your place:")
    dict1[i+1]=dict2

print(dict1)