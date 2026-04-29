print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python!")

def calculate_bmi(height, weight):
    print("Height =" + str(height))
    print("Weight =" + str(weight))

    bmi = weight / (height * height)
    print("BMI = " + str(bmi))

    if (bmi < 18.5):
        print("Underweight")
    elif (bmi >= 18.5 and bmi < 25):
        print("Normal weight")
    else:
        print("Overweight")

calculate_bmi(weight=47, height=1.58)
