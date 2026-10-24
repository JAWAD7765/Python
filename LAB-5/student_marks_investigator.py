def calculate_average(marks):
    if len(marks) == 0:
        return None

    for mark in marks:
        if not isinstance(mark, (int, float)):
            return None

        if mark < 0 or mark > 100:
            return None

    average = sum(marks) / len(marks)

    return average


def classify_performance(average):
    if average >= 80:
        return "Excellent"

    elif average >= 70:
        return "Good"

    elif average >= 60:
        return "Satisfactory"

    else:
        return "Needs Improvement"


def display_report(students):
    if len(students) == 0:
        print("No student records available")
        return

    print("ID | Name | Average | Performance")

    for student in students:
        if len(student) != 3:
            print("Invalid student record")
            continue

        student_id = student[0]
        name = student[1]
        marks = student[2]

        if not isinstance(marks, list) or len(marks) != 3:
            print(name, "- Missing or incorrect number of marks")
            continue

        average = calculate_average(marks)

        if average is None:
            print(name, "- Invalid marks")
            continue

        performance = classify_performance(average)

        print(student_id, "|", name, "|",
              round(average, 2), "|", performance)


students = [
    [201, "Amina", [78, 85, 90]],
    [202, "Rahim", [65, 70, 68]],
    [203, "Nadia", [92, 88, 95]],
    [204, "Hasan", [55, 60, 65]],
    [205, "Tania", [80, 80, 80]]
]

print("===== STUDENT MARKS REPORT =====")
display_report(students)


print("\n===== TEST EQUAL MARKS =====")

equal_marks_student = [
    [206, "Equal Marks", [80, 80, 80]]
]

display_report(equal_marks_student)


print("\n===== TEST TIED AVERAGES =====")

tied_students = [
    [207, "Student A", [70, 80, 90]],
    [208, "Student B", [75, 80, 85]]
]

display_report(tied_students)


print("\n===== TEST INVALID MARK =====")

invalid_student = [
    [209, "Invalid Mark", [90, 105, 80]]
]

display_report(invalid_student)


print("\n===== TEST NO MARKS =====")

no_marks_student = [
    [210, "No Marks", []]
]

display_report(no_marks_student)


print("\n===== TEST EMPTY STUDENT LIST =====")

display_report([])