capital_city={"nepal":"kathmandu","italy":"rome"}
print(capital_city)

capital_city["japan"]="tokyo"
print("updated Dictionary:",capital_city)          #adding elements

student_id={1:"sian",2:"siya",3:"avin"}
print("Initial Dictionary: ",student_id)
student_id[2]="Anvin"                           #change value in a dictionary
print("updated Dictionary:",student_id) 

print(student_id[3])        #accessing elements from a dictionary
print(student_id[1])

del student_id[1]
print("After deletion:",student_id)

squares={1:1,3:9,5:25,7:49,9:81}
for i in squares:
    print(squares[i])