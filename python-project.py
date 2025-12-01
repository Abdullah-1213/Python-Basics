import json

# Students dictionary
students = {
    101: {"name": "Abdullah", "marks": 85},
    102: {"name": "Shazi", "marks": 75},
    103: {"name": "Alyan", "marks": 60},
}

# Function to calculate grades
def calculate_grade(marks):
    if marks >= 85:
        return "A+"
    elif marks >= 75:
        return "B+"
    elif marks >= 60:
        return "C"
    else:
        return "F"

# Loop to add grades
for roll_no, obj in students.items():
    grade = calculate_grade(obj["marks"])
    obj["grade"] = grade

print(students)

# Save to JSON file
with open("students.json", "w") as f:
    json.dump(students, f, indent=4)
