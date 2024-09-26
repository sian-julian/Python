class Employee:
    id=10
    name="sian"

    def display(self):
        print("id: %d\nName: %s"%(self.id,self.name))
    
c=Employee()
# del c.id
# del c.name
c.display()
