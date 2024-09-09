n=8

for i in range(0,1):
    for j in range(n):
        print("* ",end='')
    print()

for i in range(1,n-1):
    for k in range(n-i-1):
        print(" ",end='')
    for j in range(n):
        if j==n-2-i:
            print(" *",end='')
        else:
            print(" ",end='')
    print()

for i in range(0,1):
    for j in range(n):
        print("* ",end='')
    print()