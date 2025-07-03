class User:
    def __init__(self, name, email):
        self.__name = name
        self.__email = email

    
    def get_info(self):
        return f"Name: {self.__name}, Email: {self.__email}"
    
    def set_email(self, new_email):
        self.__email = new_email


class Student(User):
    def __init__(self, name, email):
        super().__init__(name, email)
        self.__enrolled_courses = []

    def enroll(self, course_name):
        self.__enrolled_courses.append(course_name)

    def get_enrolled_courses(self):
        return self.__enrolled_courses
    


class Instructor(User):
    def __init__(self, name, email):
        super().__init__(name, email)
        self.__teaching_courses = []
    
    def add_course(self, course_name):
        self.__teaching_courses.append(course_name)

    def get_teaching_courses(self):
        return self.__teaching_courses
    

if __name__ == "__main__":
    student = Student("Alice", "alice@example.com")
    student.enroll("Math")
    student.enroll("Science")
    print(student.get_info())
    print("Enrolled Courses:", student.get_enrolled_courses())

    instructor = Instructor("Bob", "bob@example.com")
    instructor.add_course("History")
    instructor.add_course("Literature")
    print(instructor.get_info())
    print("Teaching Courses:", instructor.get_teaching_courses())