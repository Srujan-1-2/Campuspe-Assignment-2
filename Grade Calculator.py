subject1 = float(input("Enter marks for Subject 1: "))
subject2 = float(input("Enter marks for Subject 2: "))
subject3 = float(input("Enter marks for Subject 3: "))
subject4 = float(input("Enter marks for Subject 4: "))
subject5 = float(input("Enter marks for Subject 5: "))
print("Marks in each subject:")
print("Subject 1:", subject1)
print("Subject 2:", subject2)
print("Subject 3:", subject3)
print("Subject 4:", subject4)
print("Subject 5:", subject5)
total_marks = subject1 + subject2 + subject3 + subject4 + subject5
percentage = total_marks / 5
if percentage >= 90:
    grade = "A+ (Outstanding)"
elif percentage >= 80:
    grade = "A (Excellent)"
elif percentage >= 70:
    grade = "B (Good)"
elif percentage >= 60:
    grade = "C (Average)"
elif percentage >= 50:
    grade = "D (Pass)"
else:
    grade = "F (Fail)"
if subject1 >= 40 and subject2 >= 40 and subject3 >= 40 and subject4 >= 40 and subject5 >= 40:
    result = "Pass"
else:
    result = "Fail"
print("Total Marks (out of 500):", total_marks)
print("Percentage:", percentage)
print("Grade:", grade)
print("Result:", result)