class Student:
    def __init__(self,name,age,id):
        self.name=name
        self.age=age
        self.id=id

s=Student("Sian",21,2)

print(getattr(s,'name'))

setattr(s,"age",23)

# print(getattr(s,'age'))

print(hasattr(s,'id'))
print(hasattr(s,'place'))

delattr(s,'age')

# print(getattr(s,'age'))    #will give an error