def determine_grade(percentage):
    if percentage >= 90:
        return 'A'
    elif percentage >= 80:
        return 'B'
    elif percentage >= 70:
        return 'C'
    elif percentage >= 60:
        return 'D'
    elif percentage >= 40:
        return 'E'
    else:
        return 'F'

percentage = float(input("Enter the percentage: "))
grade = determine_grade(percentage)
print("The grade is:", grade)
