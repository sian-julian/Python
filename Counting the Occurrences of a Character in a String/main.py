str=input("Enter a String:")
ch=input("Enter a character in the String:")
count=0
for i in str:
    if(i==ch):
        count+=1

print(f"The number of occurence of {ch} is:")
