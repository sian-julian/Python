height=float(input("Enter your Height in m:"))
weight=float(input("Enter your weight in kg:"))

BMI=weight/height**2

if(BMI<18.5):
    print("Underweight")
elif(BMI<=18.5 and BMI<24.9):
    print("Normal Weight")
elif(BMI<=25 and BMI<29.9):
    print("Overweight")
elif(BMI>30):
    print("Obese")
else:
    print("invalid height or weight")