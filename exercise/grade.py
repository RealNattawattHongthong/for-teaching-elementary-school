def calculate_grade(score):
    if 90 <= score <= 100:
        grade = "A"
    elif 80 <= score < 90:
        grade = "B"
    elif 70 <= score < 80:
        grade = "C"
    elif 60 <= score < 70:
        grade = "D"
    elif 0 <= score < 60:
        grade = "F"
    else:
        grade = "Invalid score"
    return grade

# Taking user input for the student's score
try:
    score = float(input("Enter the student's score: "))
    if 0 <= score <= 100:
        student_grade = calculate_grade(score)
        print(f"The student's grade is: {student_grade}")
    else:
        print("Invalid score. Please enter a score between 0 and 100.")
except ValueError:
    print("Invalid input. Please enter a numerical score.")
