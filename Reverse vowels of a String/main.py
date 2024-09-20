def rvowel(str1):
    list1=list(str1)
    print(list1)
    vowel=['a','e','i','o','u','A','E','I','O','U']

    list2=[]
    for item in list1:
        if item in vowel:
            list2.append(item)

    print(list2)
    v_list=list2[::-1]
    print(v_list)

    v_index=0
    for item in range(len(list1)):
        if list1[item] in vowel:
            list1[item]=v_list[v_index]
            v_index+=1
    
    str2=''
    for item in list1:
        str2=str2+item
    
    print("After Reversal:",str2)
        
str1=input("Enter a String:")
rvowel(str1)









