class Parent:
    def func1(self):
        print("This is a parent class")

class Child1(Parent):
    def func2(self):
        print("This is the first Child class")

class Child2(Parent):
    def func2(self):
        print("this is the Second Child class")

o1=Child1()
o2=Child2()

o1.func1()
o1.func2()

o2.func1()
o2.func2()
