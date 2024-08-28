data=(1,2,3,5)
print(type(data))
print(data)

data2=("mouse",[8,4,6],(1,2,3))
print(data2)

data1=()        #empty tuple
print(data1)

print(data[3])
print(data2[1])
print(data[-2])

#data=data *3
#print(data)        repetition of tuples

print(data.count(1))
print(data.index(3))        #tuple methods

for i in data:
    print(i)

print(3 in data)        #check if an element exist in the tuple or not
print(7 in data2)
