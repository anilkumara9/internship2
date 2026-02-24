# Student Grade and Performance Calculator
# This program calculates the total, percentage, and grade for 5 subjects.

SUBJECT_COUNT = 5
student_marks = []

try:
    # Collecting marks for each subject iteratively
    for i in range(1, SUBJECT_COUNT + 1):
        while True:
            try:
                mark_entry = float(input(f"Enter marks for Subject {i} (0-100): "))
                if 0 <= mark_entry <= 100:
                    student_marks.append(mark_entry)
                    break
                else:
                    print("Error: Marks should be between 0 and 100.")
            except ValueError:
                print("Invalid input: Please enter a numerical value for marks.")

    # Calculating summary statistics
    total_marks_obtained = sum(student_marks)
    maximum_possible_marks = SUBJECT_COUNT * 100
    performance_percentage = (total_marks_obtained / maximum_possible_marks) * 100

    # Assigning Grades based on the percentage achieved
    if performance_percentage >= 90:
        assigned_grade = "A+"
        performance_remarks = "Outstanding Performance"
    elif performance_percentage >= 80:
        assigned_grade = "A"
        performance_remarks = "Excellent Performance"
    elif performance_percentage >= 70:
        assigned_grade = "B"
        performance_remarks = "Good Effort"
    elif performance_percentage >= 60:
        assigned_grade = "C"
        performance_remarks = "Average Performance"
    elif performance_percentage >= 50:
        assigned_grade = "D"
        performance_remarks = "Needs Improvement"
    else:
        assigned_grade = "F"
        performance_remarks = "Failed - Requires Retake"

    # Determining overall Pass/Fail status based on individual subject marks
    # Threshold for passing is usually 40 in many education systems
    has_passed_all_subjects = all(marks >= 40 for marks in student_marks)
    overall_result_status = "Pass" if has_passed_all_subjects else "Fail"

    # Displaying the performance report
    print("\n--- PERFORMANCE SUMMARY REPORT ---")
    for index, marks in enumerate(student_marks, 1):
        print(f"Subject {index}: {marks}")

    print("-" * 34)
    print(f"Total Marks Scored: {total_marks_obtained} / {maximum_possible_marks}")
    print(f"Percentage Achieved: {performance_percentage:.2f}%")
    print(f"Letter Grade      : {assigned_grade} ({performance_remarks})")
    print(f"Final Outcome     : {overall_result_status}")

except Exception as unexpected_error:
    print(f"An error occurred during calculation: {unexpected_error}")
