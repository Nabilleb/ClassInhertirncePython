class User:
    def __init__(self, name, email):
        self.__name = name
        self.__email = email

    
    def get_info(self):
        return f"Name: {self.__name}, Email: {self.__email}"
    
    def set_email(self, new_email):
        self.__email = new_email


class Student(User):
    def __init__(self, name, email, enrolled_courses):
        super().__init__(name, email)
        self.__enrolled_courses = enrolled_courses