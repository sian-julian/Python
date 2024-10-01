
class Number:
    def __init__(self,num):
        self.num=num

    def Input(self):
        self.num=int(input("Enter a number:"))
    
class Check(Number):
    def __init__(self,num):
        super().__init__(num)

    def oddeven(self):
        if self.num%2==0:
            print(f"{self.num} is a Even number")
        else:
            print(f"{self.num} is a Odd number")
 
c=Check(Number)
c.Input()
c.oddeven()



# class OddEven:
#     def Odd(self,a):
#         if a%2==0:
#             print("Even number")
#         else:
#             print("Odd number")
# b=OddEven()
# class Input:
#     a=int(input("Enter a number:"))
#     b.Odd(a)