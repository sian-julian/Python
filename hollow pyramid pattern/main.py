n=5

for i in range(n):
    for k in range(n-i-1):
        print(" ",end='')
    for j in range(i+1):
        if j==0 or j==i:
            print(" *",end='')
        else:
            print("  ",end='')
    print()

for i in range(0,1):
    for j in range(n+1):
        print("* ",end='')
    print()


