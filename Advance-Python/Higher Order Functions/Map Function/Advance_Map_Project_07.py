# Challenging Problem: Student Performance Analysis
# Story:
# You are a data analyst working for an educational platform. Your task is to evaluate the performance of students in a recent exam. You have been given a list of student dictionaries, each containing the student's name, marks in various subjects, and a boolean indicating if they passed or failed the overall exam.

# Your goal is to:

# Normalize their marks (scale the marks between 0 and 100 for each subject).
# Calculate their average marks after normalization.
# Assign grades based on their normalized average marks using the following scheme:
# 90-100: A
# 80-89: B
# 70-79: C
# 60-69: D
# Below 60: F
# Finally, update the list of dictionaries to include normalized marks, average marks, and grades for each student.


'''
Challenge:
Using the map() function:

Normalize Marks: Assume the maximum possible marks for any subject is 100, and normalize the marks for each subject by scaling them to a range of 0-100.
(In this case, normalization doesn't change values but represents real-world scenarios where scores might be scaled.)
Calculate Average Marks: Compute the average of the normalized marks for each student.
Assign Grades: Based on the average marks, assign grades using the grading scheme mentioned above.


Expected Output:
Each student's data should now include three additional fields:

normalized_marks: A dictionary of marks normalized between 0 and 100 for each subject.
average_marks: The average of the normalized marks.
grade: The grade assigned based on the average marks.


Hints:
Use a map() function to process the list of students and calculate all new fields.
Use a lambda function or helper function to normalize marks and calculate averages.
Use conditional expressions to determine grades based on the grading scheme.


'''

students = [
    {"name": "Student 1", "math": 96, "science": 37, "english": 36, "passed": True},
    {"name": "Student 2", "math": 92, "science": 42, "english": 47, "passed": True},
    {"name": "Student 3", "math": 90, "science": 91, "english": 59, "passed": True},
    {"name": "Student 4", "math": 63, "science": 31, "english": 92, "passed": True},
    {"name": "Student 5", "math": 52, "science": 45, "english": 79, "passed": False},
    {"name": "Student 6", "math": 62, "science": 82, "english": 55, "passed": False},
    {"name": "Student 7", "math": 72, "science": 78, "english": 61, "passed": False},
    {"name": "Student 8", "math": 56, "science": 84, "english": 75, "passed": True},
    {"name": "Student 9", "math": 81, "science": 49, "english": 83, "passed": False},
    {"name": "Student 10", "math": 37, "science": 91, "english": 92, "passed": True},
    {"name": "Student 11", "math": 83, "science": 77, "english": 73, "passed": False},
    {"name": "Student 12", "math": 97, "science": 43, "english": 41, "passed": True},
    {"name": "Student 13", "math": 88, "science": 53, "english": 67, "passed": True},
    {"name": "Student 14", "math": 99, "science": 97, "english": 36, "passed": False},
    {"name": "Student 15", "math": 95, "science": 47, "english": 60, "passed": True},
    {"name": "Student 16", "math": 82, "science": 86, "english": 70, "passed": False},
    {"name": "Student 17", "math": 69, "science": 96, "english": 77, "passed": True},
    {"name": "Student 18", "math": 39, "science": 92, "english": 60, "passed": False},
    {"name": "Student 19", "math": 78, "science": 79, "english": 82, "passed": False},
    {"name": "Student 20", "math": 45, "science": 38, "english": 67, "passed": False},
    {"name": "Student 21", "math": 97, "science": 76, "english": 58, "passed": True},
    {"name": "Student 22", "math": 70, "science": 85, "english": 99, "passed": False},
    {"name": "Student 23", "math": 95, "science": 64, "english": 86, "passed": True},
    {"name": "Student 24", "math": 73, "science": 73, "english": 36, "passed": False},
    {"name": "Student 25", "math": 57, "science": 75, "english": 77, "passed": False},
    {"name": "Student 26", "math": 79, "science": 94, "english": 83, "passed": False},
    {"name": "Student 27", "math": 94, "science": 40, "english": 62, "passed": False},
    {"name": "Student 28", "math": 66, "science": 55, "english": 70, "passed": True},
    {"name": "Student 29", "math": 83, "science": 73, "english": 90, "passed": True},
    {"name": "Student 30", "math": 34, "science": 92, "english": 57, "passed": True},
]

# 90-100: A
# 80-89: B
# 70-79: C
# 60-69: D
# Below 60: F

# Grading function
assign_grade = lambda Math, Science, English: (
    "A" if (avg := (Math + Science + English) / 3) >= 90 else # := is walrus operator it is used as assignment expression for example "10 Assigned" if (n := 10) and condition is checked at the same time
    "B" if avg >= 80 else
    "C" if avg >= 70 else
    "D" if avg >= 60 else
    "F"
)

    

# Assign Average Marks and Provide Grades
student_data_ = [data for data in map(
    lambda metadata: 
    {
        **metadata,
        "average_marks":round((metadata["math"]+metadata["english"]+metadata["science"])/3,3),
        "grade": assign_grade(metadata["math"],metadata["science"],metadata["english"]),
    }
    ,students
)]


"[.] Additional"

# we can observer that some student with F grade have passed=True and some student with grade grade other than F have passed=False
# we can enhance the data quality by normalizing the passed status on the behalf of grade

update_status = lambda grade, passed: (
    False if grade == "F" and passed else
    True if grade != "F" and not passed else
    passed
)

normalized_student_data = [
    print(data) for data in map(
        lambda metadata: {**metadata, "passed":update_status(metadata["grade"],metadata["passed"])},student_data_
    )
]
