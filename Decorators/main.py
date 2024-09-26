# EXMAPLE 1

# def strupper(func):
#     def inner():
#         str2=func()
#         return str2.upper()
#     return inner

# @strupper
# def str1():
#     return "good morning"

# print(str1())



#EXMAPLE 2

# def divdec(func):
#     def inner(x,y):
#         if y<1:
#             return "Division by Zero or Negative number is not possible"
#         return func(x,y)
#     return inner

# @divdec
# def divide(a,b):
#     return a//b

# print(divide(4,0))




#Multiple Decorators on a single function

#Example 

# def strupper(func):
#     def inner():
#         str2=func()
#         return str2.upper()
#     return inner

# def splits(func):
#     def wrapper():
#         str3=func()
#         return str3.split()
#     return wrapper

# @splits
# @strupper
# def str1():
#     return "good morning"
# print(str1())


#What if the Decorator contains parameter?

#Exmaple

def outer(expr):
    def dec(func):
        def inner():
            return func() + expr
        return inner
    return dec

@outer("sian")
def ordinary():
    return "good morning "

print(ordinary())







