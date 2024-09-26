class Calculation1:
    def add(self,a,b):
        return a+b

class Calculation2:
    def sub(self,a,b):
        return a-b

class Calculation3:
    def multiply(self,a,b):
        return a*b
    
class ChildCalculation(Calculation1,Calculation2,Calculation3):
    def divide(self,a,b):
        return a//b

c1=ChildCalculation()
print(c1.add(10,20))
print(c1.sub(20,10))
print(c1.multiply(20,2))
print(c1.divide(20,4))

    
