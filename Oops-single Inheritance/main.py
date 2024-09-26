class Animal:
    def speak(self):
        print("Animal alert!!")
    
class dog(Animal):
    def bark(self):
        print("Dog barking")

d=dog()
d.speak()
d.bark()