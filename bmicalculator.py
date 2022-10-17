height = input("enter your height in meters: ")
weight = input("enter your weight in kilograms: ")


print(height)
print(weight)


weight_as_int = int(weight)
height_as_float = float(height)


bmi = round(weight_as_int / height_as_float ** 2)

if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are under weight. ")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight. Good job!")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are overweight. ")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese. ")
else:
    print(f"Your BMI is {bmi}, you are clinicly obese. See a doctor")


