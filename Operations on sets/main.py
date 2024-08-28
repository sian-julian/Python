months=set(["jan","feb","mar","apr","may","june"])
print(months)
months.add("july")              #can be used to add a single element
print(months)

months.update(["dec","oct"])    #can be used to add Multiple elements
print(months)

months.discard("jan")
print(months)
                                #can be used to remove elements from a set(only single values can be removed)
months.remove("feb")
print(months)

days1={"mon","tue","wed","thu","fri","sat","sun"}
print(months|days1)                                  #Union of sets

days2={"thu","fri","sat","sun"}
print(days1&days2)                                  #Intersction of sets

#print(days1>days2)
#print(days2>days1)
#print(days1==days2)                #Comparison of sets(return true or false value)