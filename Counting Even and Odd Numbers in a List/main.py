a=[24,35,2,4,28,9,6,5,9,10]
even=0
odd=0

for i in a:
    if(i%2==0):
        even+=1
    else:
        odd+=1

print("Number of Even numbers:",even)
print("Number of Odd numbers:",odd)
