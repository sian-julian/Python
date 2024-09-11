og_set=set()
# print(type(str))
n=int(input("Enter the size of the set:"))

for i in range(n):
    item=input()
    og_set.add(item)

print("Original Set:",og_set)

vowel_set={char for item in og_set for char in item if char in 'aeiouAEIOU'}

print("Set with Unique vowels:",vowel_set)