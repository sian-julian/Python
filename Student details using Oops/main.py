
class Student():
    def __init__(self):
        self.list1=[]

    def student(self):
        dif={}

        dif['name']=input("Enter your name:")
        dif['rollno']=int(input("Enter your roll no:"))
        dif['address']=input("Enter your Address:")
        print()
        self.list1.append(dif)
        print("Student Added Successfully!!")

class Details(Student):
    def __init__(self):
        super().__init__()
        
    def displaydetails(self):
        if self.list1:
            for dif in self.list1:
                print(f"Name: {dif['name']}")
                print(f"Roll No: {dif['rollno']}")
                print(f"Address: {dif['address']}")
                print()
            else:
                print("No Students Added!!")


d=Details()
d.student()
d.displaydetails()
