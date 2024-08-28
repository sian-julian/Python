mixed_list=[10,20.5,3+4j,"Python"]
list2=[100,200]

mixed_list.append("Programming")
print("After Appending:",mixed_list)

mixed_list.extend(list2)
print("After Extension:",mixed_list)

print("Last Element of the list:",mixed_list[6])