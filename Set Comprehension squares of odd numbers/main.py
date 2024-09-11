og_set=set()

for i in range(1,16):
    og_set.add(i)

print("Original set:",og_set)

sq_set={item**2 for item in og_set if item % 2!=0}
print("The Odd Square set:",sq_set)
