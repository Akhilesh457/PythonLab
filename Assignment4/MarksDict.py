students = {
    "Akhilesh": 85,
    "Ravi": 92,
    "Neha": 78,
    "Priya": 88
}

highest = max(students, key=students.get)
lowest = min(students, key=students.get)

print("Highest Marks:", highest, "-", students[highest])
print("Lowest Marks:", lowest, "-", students[lowest])
