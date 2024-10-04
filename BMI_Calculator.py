name= input("Enter your Name: ")

weight = int(input("Enter your weight: "))
height = int(input("Enter your height: "))
BMI = (weight)/(height * height)

print(BMI)

if(BMI > 0):
    if(BMI < 18.5):
        print(f"{name} You are underweight.")
    elif(BMI <=24.9):
        print(f"{name}, you are normal weight")
    elif(BMI <29.9):
        print(f"{name}, you are overweight")
    elif(BMI <34.9):
        print(f"{name} you are obese")
    elif(BMI <39.9):
        print(f"{name}, you are severely obese")
    else:
        print("You are morbidely obese")
else:
    print("Enter valid input")



# BMI Categories:
# Underweight = <18.5
# Normal weight = 18.5–24.9
# Overweight = 25–29.9
# Obesity = BMI of 30 or greater