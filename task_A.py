def calculate_grade(score):
    if score >= 90:
        return 'A'
    elif 80 <= score < 90:
        return 'B'
    elif 70 <= score < 80:
        return 'C'
    elif 60 <= score < 70:
        return 'D'
    else:
        return 'F'

print("Enter Student Name:")
name = input()
print("Enter Roll No.")
roll_number = input()
print("Enter marks in Maths:")
maths_score = int(input())
print("Enter marks in Physics:")
physics_score = int(input())
print("Enter marks in Chemistry:")
chemistry_score = int(input())

maths_grade = calculate_grade(maths_score)
physics_grade = calculate_grade(physics_score)
chemistry_grade = calculate_grade(chemistry_score)

overall_grade = calculate_grade((maths_score + physics_score + chemistry_score) // 3)

print("--------------------")
print("Here is the Grade Card:")
print("--------------------")
print("Student Name:", name)
print("Student Roll:", roll_number)
print("Grade in Maths:", maths_grade)
print("Grade in Physics:", physics_grade)
print("Grade in Chemistry:", chemistry_grade)
print("Overall Grade:", overall_grade)
print("--------------------")
print("Thank you!")
