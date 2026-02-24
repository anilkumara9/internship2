# Student Personal Bio Card Program
# This program stores student information in variables and displays it in a formatted card.

# Student Information Variables
student_name = "John Doe"
student_age = "20 years"
enrolled_course = "Python Programming"
target_college = "ABC University"
contact_email = "john@example.com"

# Displaying the Bio Card with a decorative border
print("╔══════════════════════════════════════════════════╗")
print("║                STUDENT BIO CARD                  ║")
print("╠══════════════════════════════════════════════════╣")
print("║                                                  ║")
print(f"║  Name    : {student_name:<33} ║")
print(f"║  Age     : {student_age:<33} ║")
print(f"║  Course  : {enrolled_course:<33} ║")
print(f"║  College : {target_college:<33} ║")
print(f"║  Email   : {contact_email:<33} ║")
print("║                                                  ║")
print("╚══════════════════════════════════════════════════╝")
