n=8

for i in range(n):
    if i==0:
        for j in range(n-2):
            print("* ",end='')
        print()
    else:
        if i<n-4:
            for j in range(n):
                if j==0:
                    print("* ",end='')
            print()
        elif i==4:
            for j in range(n-2):
                if j==1:
                    print("  ",end='')
                else:
                    print("* ",end='')
            print()
        elif i<7:
            for j in range(n):
                if j==0 or j==n-3:
                    print("* ",end='')
                else:
                    print("  ",end='')
            print()
        elif i==7:
            for j in range(n-2):
                print("* ",end='')

                

