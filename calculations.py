conversion = {
    'A+': 4.3,
    'A': 4.0,
    'A-': 3.7,
    'B+': 3.3,
    'B': 3.0,
    'B-': 2.7,
    'C+': 2.3,
    'C': 2.0,
    'C-': 1.7,
    'D+': 1.3,
    'D': 1.0,
    'D-': .7,
    'F': 0.0
}


def calculate(previous_gpa: float,previous_credits: float, grades: list, credit: list):
    current_credits = previous_credits
    current_numerator = previous_gpa * previous_credits
    for i, grade in enumerate(grades):
        current_credits += credit[i]
        current_numerator += conversion[grade] * credit[i]

    print(current_numerator / current_credits)

