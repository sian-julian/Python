a=input("Enter a String:")
length=len(a)
rev=""

for i in range(length):
    rev=a[i]+rev
print(rev)

