def is_anagram(s1,s2):
    s1=sorted(s1)
    s2=sorted(s2)
    if s1==s2:
        print("Is anagram")
    else:
        print("Not anagram")

s1=input("Enter the first word: ")
s2=input("Enter the second word: ")
is_anagram(s1,s2)