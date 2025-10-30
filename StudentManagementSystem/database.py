from utils import load_data, save_data

def add_student():
    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")
    course = input("Enter course: ")

    student_data = f"{roll_no},{name},{course}\n"
    save_data(student_data)
    print(f"Student {name} added successfully!")

def view_students():
    students = load_data()
    if not students:
        print("No students found.")
        return
    print("\n--- Student List ---")
    for s in students:
        roll_no, name, course = s.strip().split(',')
        print(f"Roll No: {roll_no} | Name: {name} | Course: {course}")

def search_student():
    students = load_data()
    roll_no_to_search = input("Enter roll number to search: ")
    for s in students:
        roll_no, name, course = s.strip().split(',')
        if roll_no == roll_no_to_search:
            print(f"Found: {name} ({course})")
            return
    print("Student not found.")
