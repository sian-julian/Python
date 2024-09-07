n=5

for i in range(n):
    for k in range(i):
        print(" ",end='')
    for j in range(n-i):
        print("* ",end='')
    print()

for i in range(n-1):
    for k in range(n-2-i):
        print(" ",end='')
    for j in range(i+2):
        print("* ",end='')
    print()
