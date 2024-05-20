#Activity 3 
#Grade Calculator
#user input Subject
subject = input("Enter your subject name: ")
#user input marks in the subject
marks = int(input(f'Enter your marks in {subject}: '))

# find out grade according to student marks in the subject
if marks < 50:
    grade = "FAIL"
elif marks < 65:
    grade = "PASS"
elif marks < 75:
    grade = "CREDIT"
elif marks < 85:
    grade = "DIST"
else:
    grade = "HD"

# Display the grade in the subject
print(f'Your grade in {subject} is {grade}')
