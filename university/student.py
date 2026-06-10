
class Student():
    """Represents the students with basic details."""


    def __init__(self, name, id):
        self.name= name
        self.id= id

        self.courses = {}

    def add_course(self, course_id):
        self.courses[course_id] = None

    def add_mark(self, course_id, mark):
        self.courses[course_id] = mark


    def get_gpa(self):
        pass

    def __str__(self):
        s = "=======================\n"
        s += f"name: {self.name}, id:{self.id}\n"
        s += f"GPA: {self.get_gpa()}\n"
        s += f"Courses: {str(self.courses)}\n"
        s += "======================="
        return s
    
    

def main():
    """This is a test function for student class"""

    print("test1: ")
    s1 = Student("John Doh", 1001)
    s1.add_course("S13454546")
    s1.add_course("S24678978")
    print(s1)

if __name__ == "__main__":
    main()

