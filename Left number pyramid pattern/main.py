n=5
cnt=1
cnt2=2

for i in range(n):
    for j in range(i+1):                    
        print(f"{j+1} ",end='')
    print()

print()

for i in range(n):
    for j in range(i+1):
        print(f"{cnt} ",end='')
        cnt+=1
    print()

print()

for i in range(n):
    for j in range(i+1):
        print(f"{cnt} ",end='')
        cnt+=2
    print()

print()

for i in range(n):
    for j in range(i+1):
        print(f"{cnt2} ",end='')
        cnt2+=2
    print()