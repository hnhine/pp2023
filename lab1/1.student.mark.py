
#function to enter students information
def input_Student_info():
    total_stu = int(input("Enter total number of students in class: "))
    list_student = {"ID": [], "Fullname": [], "DoB": []}

    for i in range(int(total_stu)):
        print("Information of student ",i," :")
        id = input("Enter student ID: ")
        name = input("Enter student full name: ")
        DoB = input("Enter date of birth: ")
        list_student["ID"].append(id)
        list_student["Fullname"].append(name)
        list_student["DoB"].append(DoB)
    return list_student

list_students = input_Student_info()
print(list_students)

#function to enter course information
def course_infor():
    total_courses = int(input("Enter total number of courses: "))
    list_courses = {"ID": [], "Course_Name": []}
    for i in range(total_courses):
        print("Input course's information ",i+1)
        id = input("Enter course ID: ")
        name = input("Enter course name: ")
        list_courses["ID"].append(id)
        list_courses["Course_Name"].append(name)
    return list_courses
list_courses = course_infor()
print(list_courses)
#main_list = np.array(())

#function to enter  mark for courses
def input_mark(list_students, list_courses):
    number_course_input = int(input("Enter total course you want to input mark: "))
    nested_course_mark = {"Course_id": [], 'Student_ID' : [], 'Mark': []}
    for k in range(number_course_input):
        course_id = input("Enter course ID: ")
        if (course_id in list_courses["ID"]):
            nested_course_mark['Course_id'].append(course_id)
            for i in range(len(list_students['ID'])):
                nested_course_mark['Student_ID'].append(list_students["ID"][i])
                print("Enter the mark of student ", list_students["ID"][i]," :")
                m = float(input())
                nested_course_mark['Mark'].append(m)

        else:
            print("That's course not exit!")
    return nested_course_mark
mark_sheet = input_mark(list_students, list_courses)

#function to show mark of a give course
def show_mark(course_id, mark_sheet):
    if course_id in mark_sheet["Course_id"]:
        index_course_id = 0
        for k in range(len(mark_sheet["Student_ID"])):
            if mark_sheet["Course_id"][k] == course_id:
                index_course_id = k
                break
        print(mark_sheet['Course_id'][index_course_id])
        for i in range(int(len(mark_sheet['Student_ID'])/len(mark_sheet['Course_id']))):
            #print(mark_sheet['Course_id'][index_course_id])
            print(mark_sheet['Student_ID'][index_course_id+i],": ",mark_sheet['Mark'][index_course_id+i])

#listing function for mark of a given course
show_mark('ict1', mark_sheet)