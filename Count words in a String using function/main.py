def count_words(s):
    count=1
    for i in range(length):
        if s[i]==" ":
            count+=1
    return (count)
s=input("Enter the sentence: ")
length=len(s)
print("Count: ",count_words(s))