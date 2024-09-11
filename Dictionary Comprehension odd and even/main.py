numbers=[]

for i in range(1,11):
    numbers.append(i)

values=["True" if num % 2==0 else "False" for num in numbers]
print(values)

dict1={k:v for (k,v) in zip(numbers,values)}
print("The Dictionary:",dict1)