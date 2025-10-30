FILE_PATH = "Students.txt"

def load_data():
    try:
        with open(FILE_PATH, "r") as file:
            return file.readlines()
    except FileNotFoundError:
        return []

def save_data(student_data):
    with open(FILE_PATH, "a") as file:
        file.write(student_data)

