class Entity:
    def __init__(self, id, name):
        self.__id = id
        self.__name = name
    def getID(self):
        return self.__id
    def getName(self):
        return self.__name
    def setName(self, name):
        self.__name = name
class Student(Entity):
    def __init__(self, student_id, name, dob):
        super().__init__(student_id, name)
        self.__dob = dob
    def getDob(self):
        return self.__dob
    def setDob(self, dob):
        self.__dob = dob

class ListStudent:
    def __init__(self):
        self.__length = 0
        self.__list:list[Student] = []
    def getList(self):
        return self.__list
    def insert(self, s: Student):
        for i in self.__list:
            if i.getID() == s.getID():
                print("This id exists!\n")
                return 0
        self.__list.append(s)
        self.__length += 1
        return 1
    def display (self):
        print("student_id             fullname             DoB  \n")
        for i in self.__list:
            print(f"{i.getID():23}{i.getName():21}{i.getDob():5}\n")

class Course(Entity):
    def __init__(self, course_id, name):
        super().__init__(course_id, name)
    
class ListCourse():
    def __init__(self):
        self.__length = 0
        self.__list:list[Course] = []
    def getList(self):
        return self.__list
    def insert(self, s: Course):
        for i in self.__list:
            if i.getID() == s.getID():
                print("This course id exists!\n")
                return 0
        self.__list.append(s)
        self.__length += 1
        return 1
    def display (self):
        print("course_id             name\n")
        for i in self.__list:
            print(f"{i.getID():22}{i.getName():10}\n")

class Mark:
    def __init__(self, course_id, student_id, mark):
        self.__course_id = course_id
        self.__student_id = student_id
        self.__mark = mark
    def getMark(self):
        return self.__mark
    def setMark(self, mark):
        self.__mark = mark
    def getCourseid(self):
        return self.__course_id
    def getStudentid(self):
        return self.__student_id
class Marksheet:
    def __init__(self):
        self.__length = 0
        self.__list:list[Mark] = []
    def insert(self, m: Mark):
        for i in self.__list:
            if i.getCourseid() == m.getCourseid() and i.getStudentid() == m.getStudentid():
                print("Invalid!!!\n")
                return 0
        self.__list.append(m)
        self.__length +=1
        return 1
    def display(self, course_id):
        for i in self.__list:
            if i.getCourseid() == course_id:
                print("course_id             student_id             mark\n")
                print(f"{i.getCourseid():22}{i.getStudentid():23}{i.getMark():4}\n")

class Main:
    def __init__(self,total_student, total_course):
        self.__total_student = total_student
        self.__total_course = total_course
        self.__student_list:ListStudent = ListStudent()
        self.__course_list:ListCourse = ListCourse()
        self.__mark_sheet:Marksheet = Marksheet()
    def add_student(self):
        for i in range(self.__total_student):
            while True:
                s_id = input(f"Enter student id {i+1} :\n")
                s_name = input(f"Enter student name {i+1} :\n")
                s_dob = input(f"Enter student dob {i+1} :\n")
                s = Student(s_id, s_name, s_dob)
                if (self.__student_list.insert(s) ==1):
                    break
    def add_course(self):
        for i in range(self.__total_course):
            while True:
                c_id = input(f"Enter course id {i+1} :\n")
                c_name = input(f"Enter course name {i+1} :\n")
                c = Course(c_id, c_name)
                if self.__course_list.insert(c) == 1:
                    break
    def input_mark(self):
        for i in self.__course_list.getList():
            for k in self.__student_list.getList():
                while True:
                    m = float(input(f"Enter mark for course {i.getID()} of student {k.getID()}: \n"))
                    r_mark = Mark(i.getID(), k.getID(), m)
                    if self.__mark_sheet.insert(r_mark) == 1:
                        break
    def display_student_list(self):
        self.__student_list.display()
    def display_course_list(self):
        self.__course_list.display()
    def display_mark(self):
        course_id = input("Enter course id you want to show mark: \n")
        self.__mark_sheet.display(course_id)

ntt = Main(2,2)
ntt.add_student()
ntt.display_student_list()
ntt.add_course()
ntt.display_course_list()
ntt.input_mark()
ntt.display_mark()
ntt.display_mark()