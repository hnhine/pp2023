class Entity:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Student(Entity):
    def __init__(self, student_id, name, dob):
        super().__init__(student_id, name)
        self.dob = dob

class ListStudent:
    def __init__(self):
        self.length = 0
        self.list:list[Student] = []
    
    def insert(self, s: Student):
        for i in self.list:
            if i.id == s.id:
                print("This id exists!\n")
                return 0
        self.list.append(s)
        self.length += 1
        return 1
    def display (self):
        print("student_id             fullname             DoB  \n")
        for i in self.list:
            print(f"{i.id:23}{i.name:21}{i.dob:5}\n")

class Course(Entity):
    def __init__(self, course_id, name):
        super().__init__(course_id, name)
class ListCourse():
    def __init__(self):
        self.length = 0
        self.list:list[Course] = []
    def insert(self, s: Course):
        for i in self.list:
            if i.id == s.id:
                print("This course id exists!\n")
                return 0
        self.list.append(s)
        self.length += 1
        return 1
    def display (self):
        print("course_id             name\n")
        for i in self.list:
            print(f"{i.id:22}{i.name:10}\n")

class Mark:
    def __init__(self, course_id, student_id, mark):
        self.course_id = course_id
        self.student_id = student_id
        self.mark = mark
class Marksheet:
    def __init__(self):
        self.length = 0
        self.list:list[Mark] = []
    def insert(self, m: Mark):
        for i in self.list:
            if i.course_id == m.course_id and i.student_id == m.student_id:
                print("Invalid!!!\n")
                return 0
        self.list.append(m)
        self.length +=1
        return 1
    def display(self, course_id):
        for i in self.list:
            if i.course_id == course_id:
                print("course_id             student_id             mark\n")
                print(f"{i.course_id:22}{i.student_id:23}{i.mark:4}\n")

class Main:
    def __init__(self,total_student, total_course):
        self.total_student = total_student
        self.total_course = total_course
        self.student_list:ListStudent = ListStudent()
        self.course_list:ListCourse = ListCourse()
        self.mark_sheet:Marksheet = Marksheet()
    def add_student(self):
        for i in range(self.total_student):
            while True:
                s_id = input(f"Enter student id {i+1} :\n")
                s_name = input(f"Enter student name {i+1} :\n")
                s_dob = input(f"Enter student dob {i+1} :\n")
                s = Student(s_id, s_name, s_dob)
                if (self.student_list.insert(s) ==1):
                    break
    def add_course(self):
        for i in range(self.total_course):
            while True:
                c_id = input(f"Enter course id {i+1} :\n")
                c_name = input(f"Enter course name {i+1} :\n")
                c = Course(c_id, c_name)
                if self.course_list.insert(c) == 1:
                    break
    def input_mark(self):
        for i in self.course_list.list:
            for k in self.student_list.list:
                while True:
                    m = float(input(f"Enter mark for course {i.id} of student {k.id}: \n"))
                    r_mark = Mark(i.id, k.id, m)
                    if self.mark_sheet.insert(r_mark) == 1:
                        break
    def display_student_list(self):
        self.student_list.display()
    def display_course_list(self):
        self.course_list.display()
    def display_mark(self):
        course_id = input("Enter course id you want to show mark: \n")
        self.mark_sheet.display(course_id)

ntt = Main(2,2)
ntt.add_student()
ntt.display_student_list()
ntt.add_course()
ntt.display_course_list()
ntt.input_mark()
ntt.display_mark()
ntt.display_mark()