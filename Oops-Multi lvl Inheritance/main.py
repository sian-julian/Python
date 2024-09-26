class Animal:
    def speak(self):
        print("Animal alert!!")
    
class Dog(Animal):
    def bark(self):
        print("Dog barking")

class Dogchild(Dog):
    def eat(self):
        print("Dog Eating")

d=Dogchild()
d.speak()
d.bark()
d.eat()