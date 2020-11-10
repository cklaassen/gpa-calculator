from calculations import calculate

priorGPA = 0
priorCredits = 0
taken = input("Have you taken prior courses y/n: ")
if taken.lower() == 'y':
    priorGPA = input("What has been your previous GPA: ")
    priorCredits = input("How many credits have you taken: ")

grade = input("Enter in the grade achieved in your class (type \'exit\' to calculate): ")
creditsForClass = input("How many credits was this course: ")
gradesList = []
creditsList = []

while not grade.lower() == 'exit':
    gradesList.append(grade)
    creditsList.append(float(creditsForClass))
    grade = input("Enter in the grade achieved in your class (type \'exit\' to calculate): ")
    if not grade.lower() == 'exit':
        creditsForClass = input("How many credits was this course: ")

calculate(float(priorGPA), float(priorCredits), gradesList, creditsList)
