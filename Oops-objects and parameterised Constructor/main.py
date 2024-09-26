class Car:
    def __init__(self,modelname,year):              #parameterised Constructer
        self.modelname=modelname
        self.year=year
        
    def display(self):
        print(f"Car Model: {self.modelname}\nYear: {self.year}")

c1=Car("Toyota",2013)
c1.display()
        