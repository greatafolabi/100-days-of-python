# Grading System - Convert Scores to Letter Grades

# Dictionary of student scores
student_scores = {
    "Harry": 88,
    "Ron": 78,
    "Hermione": 95,
    "Draco": 75,
    "Neville": 62
}

# Empty dictionary to store grades
student_grades = {}

# Loop through each student and assign grade based on score
for student in student_scores:
    score = student_scores[student]
    
    # Grade assignment logic
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Exceeds Expectations"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

# Print the results
print("Student Grades:")
print(student_grades)

# Alternative: Print formatted results
print("\n=== Grade Report ===")
for student in student_grades:
    print(f"{student}: {student_grades[student]} (Score: {student_scores[student]})")
