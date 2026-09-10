# Program to calculate student total weighted exam points

# Input section
last_name = input("Enter student's last name: ")
midterm_score = float(input("Enter midterm exam score (0 - 100): "))
final_score = float(input("Enter final exam score (0 - 100): "))

# Processing section
total_points = (0.40 * midterm_score) + (0.60 * final_score)

# Output section
print(f"\nStudent Last Name: {last_name}")
print(f"Total Exam Points: {total_points:.1f}")
