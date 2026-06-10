
"""Simple database IO for university"""

from student import Student
from course import Course

STUDENT_DATABASE = "./data/student.csv"

# student: id, name, course1: mark, course2: mark

def write_student(student):

    with open(STUDENT_DATABASE, "a") as f: 
        s = f"{student.id},{student.name}"


        for k,v in student.courses.items():
            s += f",{k}:{v}"

        s += "\n"

        f.write(s)


def main():

    s1 = Student("John Doh", 1001)
    s1.add_course("S13454546")
    s1.add_course("S24678978")
    print(s1)

    s2 = Student("John Doh", 1002)
    s2.add_course("S13454546")
    s2.add_course("S24678978")
    print(s1)

    write_student(s1)
    write_student(s2)

if __name__ == "__main__":
    main()