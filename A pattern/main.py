n=8

for i in range(n):
    if i==n//2:
        for k in range(n-i-1):
            print(" ",end='')
        for j in range(n-3):
            print("* ",end='')
        print()
    else:
        for k in range(n-i-1):
            print(" ",end='')
        for j in range(i+1):
            if j==0 or j==i:
                print("* ",end='')
            else:
                print("  ",end='')
        print()        