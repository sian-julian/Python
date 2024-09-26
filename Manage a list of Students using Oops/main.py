class Student:
    def __init__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade

    def display_details(self):
        print(f"Student's Name: {self.name}")
        print(f"Student's Age: {self.age}")
        print(f"Student's Grade: {self.grade}")
        print()

class Menu:
    def __init__(self):
        self.students=[]

    def add_student(self):
        name=input("Enter the Student's name:")
        age=int(input("Enter the Student's age:"))
        grade=input("Enter the Student's grade:")   
        student=Student(name,age,grade)
        self.students.append(student)
        print("Student Added Successfully!!\n")
    
    def display_students(self):
        if self.students:
            for student in self.students:
                student.display_details()
        else:
            print("No Students have been added!!")
            print()


m=Menu()

while True:
    print("***MANAGE LIST OF STUDENTS***\n")
    print("1.Add Students\n2.Display Students Details\n3.Exit")
    ch=int(input("Enter your choice:"))

    if ch==1:
        m.add_student()
    elif ch==2:
        m.display_students()
    elif ch==3:
        print("Exiting from the program....")
        break
    else:
        print("INVALID CHOICE....try again")
        print()
    