def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 40:
        return "D"
    else:
        return "F"

# Testing the function with given marks
print("Grade for 95:", calculate_grade(95))  # A
print("Grade for 72:", calculate_grade(72))  # C
print("Grade for 59:", calculate_grade(59))  # D
print("Grade for 30:", calculate_grade(30))  # F
