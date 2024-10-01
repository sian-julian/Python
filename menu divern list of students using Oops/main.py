class Student:
    def __init__(self):
        # self.name=name
        # self.rollno=rollno
        # self.m1=m1
        # self.m2=m2
        # self.m3=m3
        self.students=[]
    
    def addstudent(self):
        print("**Add a new Student**\n")
        student={}
        student['name']=input("Enter the Student's name:")
        while True:
            rn=int(input("Enter the Student's roll no:"))
            if any(student['rollno']==rn for student in self.students):
                print("roll no already exists...try another roll no")
            else:
                student['rollno']=rn
                break
        
        student['maths']=int(input("Enter the marks in maths:"))
        student['science']=int(input("Enter the marks in science:"))
        student['english']=int(input("Enter the marks in english:"))
        
        self.students.append(student)
        print("Student Added Successfully!!\n")

    def displaystudents(self):
        print("**Display all students**\n")
        if self.students:
            for i,student in enumerate(self.students,start=1):
                print(f"Student {i}")
                print(f"Student name: {student['name']}")
                print(f"student rollno: {student['rollno']}")
                print(f"marks in maths: {student['maths']}")
                print(f"marks in science: {student['science']}")
                print(f"marks in english: {student['english']}")
                print()
            
        else:
            print("No Students Added!!")
            print()
    

    def updatest(self):
        print("**Update Student's marks**\n")
        if self.students:
            rn=int(input("Enter the student's rollno:"))
            found=False

            for student in self.students:
                if student['rollno']==rn:
                    student['maths']=int(input("Enter new marks in maths:"))
                    student['science']=int(input("Enter new marks in science:"))
                    student['english']=int(input("Enter new marks in english:"))
                    print("Marks updated successfully!!")
                    found=True
                    break

            if found==True:
                print()
            else:
                print("Student not found!!\n")
        else:
            print("No Student's added!!")
            print()
    

    def avgstudent(self):
        print("**Average marks of the student**\n")
        
        if self.students:
            rn=int(input("Enter the student's rollno:"))
            found=False

            for student in self.students:
                if student['rollno']==rn:
                    avg=float((student['maths'] + student['science'] + student['english'])/3)
                    print("Average marks of the student is: ",avg)
                    found=True
                    break
            
            if found==True:
                print()
            else:
                print("Student not found!!\n")
        else:
            print("No student's added!!\n")
        
        
s=Student()

while True:
    print("***MANAGE LIST OF STUDENTS***\n")
    print("1.Add a new student\n2.View all students\n3.Update marks of a student\n4.Calculate and display the average marks of a student\n5.Exit.")
    ch=int(input("Enter your choice:"))

    if ch==1:
        s.addstudent()
    elif ch==2:
        s.displaystudents()
    elif ch==3:
        s.updatest()
    elif ch==4:
        s.avgstudent()
    elif ch==5:
        print("Exiting from the program....")
        break
    else:
        print("INVALID CHOICE....try again")
        print()