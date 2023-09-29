#advance
def calculate_bmi(weight, height, age):
    bmi = weight / (height ** 2)
    if age < 18:
        bmi_category = "BMI categories for children and teenagers are different. Consult a healthcare professional."
    elif 18 <= age < 24:
        bmi_category = "For adults aged 18-24:"
    elif 24 <= age < 34:
        bmi_category = "For adults aged 24-34:"
    elif 34 <= age < 44:
        bmi_category = "For adults aged 34-44:"
    elif 44 <= age < 54:
        bmi_category = "For adults aged 44-54:"
    elif 54 <= age:
        bmi_category = "For adults aged 54 and above:"
    else:
        bmi_category = "Invalid age input."
    
    if bmi < 18.5:
        bmi_label = "Underweight"
    elif 18.5 <= bmi < 24.9:
        bmi_label = "Normal weight"
    elif 25 <= bmi < 29.9:
        bmi_label = "Overweight"
    else:
        bmi_label = "Obese"
    
    return f"Your BMI is {bmi:.2f}. {bmi_category} You are {bmi_label}."

# Taking user input
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))
age = int(input("Enter your age in years: "))

# Calculating and displaying BMI
result = calculate_bmi(weight, height, age)
print(result)
