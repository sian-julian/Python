n=4
p=10

for i in range(n):
    for j in range(i+1):
        print("*",end='')
    
    for j in range(2*(n-i)):
        print(" ",end='')
    
    for j in range(i+1):
        print("*",end='')
    print()


for i in range(0,1):
    for j in range(p):
        print("*",end='')
    print()  

for i in range(n):
    for j in range(n-i):
        print("*",end='')
     
    for j in range(2*(i+1)):
        print(" ",end='')
    
    for j in range(n-i):
        print("*",end='')
    print()