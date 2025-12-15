class Department:
    def __init__(self, dept_name):
        self.dept_name = dept_name


class Course:
    def __init__(self, course_name, department):
        self.course_name = course_name
        self.department = department


class Student:
    def __init__(self, student_name):
        self.student_name = student_name

    def enroll(self, course):
        print("Student:", self.student_name)
        print("Enrolled in Course:", course.course_name)
        print("Department:", course.department.dept_name)


# Driver code
dept = Department("Computer Science")
course = Course("Data Structures", dept)
student = Student("Akhilesh")

student.enroll(course)
