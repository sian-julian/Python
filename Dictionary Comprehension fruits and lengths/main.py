fruits= ['apple', 'banana', 'cherry', 'date']
lengths=[]

for i in fruits:
    lengths.append(len(i))

dict1={k:v for (k,v) in zip(fruits,lengths)}

print(dict1)
