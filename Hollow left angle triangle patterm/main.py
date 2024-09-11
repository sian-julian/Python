n=5

for i in range(n):
    if i<n-1:
        for j in range(i+1):
            if j==0 or j==i:
                print("* ",end='')
            else:
                print("  ",end='')
        print()      
    elif i<n:
        for j in range(n):
            print("* ",end='')
        print()  