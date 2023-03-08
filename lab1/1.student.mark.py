
#function to enter students information
def input_Student_info():
    total_stu = int(input("Enter total number of students in class: "))
    list_student = {"ID": [], "Fullname": [], "DoB": []}

    for i in range(int(total_stu)):
        print("Information of student ",i + 1," :")
        id = input("Enter student ID: ")
        name = input("Enter student full name: ")
        DoB = input("Enter date of birth: ")
        list_student["ID"].append(id)
        list_student["Fullname"].append(name)
        list_student["DoB"].append(DoB)
        print("")
    return list_student


#function to show list students
def show_students(list_students):
    print("The list of students: ")
    print(f" {'id'}             {'fullname'}              {'DoB'}  ")
    for i in range(len(list_students['ID'])):
        print(f"{list_students['ID'][i]}   {list_students['Fullname'][i]}{'      '}{list_students['DoB'][i]}")

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

#function to show course infor
def show_course(list_course):
    print("The list of courses: ")
    print(f" {'id'}             {'course_name'} ")
    for i in range(len(list_course['ID'])):
        print(f"{list_course['ID'][i]}             {list_course['Course_Name'][i]}")


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


#two function for showing mark
def part_show_mark(course_id, mark_sheet):
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
def show_mark(mark_sheet):
    course_id = input("Enter the course id you want to show mark: ")
    part_show_mark(course_id, mark_sheet)

def main_command():
    print(
        """
        i1  : input student information
        i2  : input course information
        i3  : enter mark for a given course
        s1  : show student information
        s2  : show course information
        s3  : show mark for a given course
        e   : exit
        """
    )
def main():

    while True:
        main_command()
        cd = input("Choose your action: ").lower()

        if cd == 'i1':
            list_students = input_Student_info()
            print("Now, you have the students list. Choose next action!")
        elif cd == 'i2':
            list_courses = course_infor()
            print("Now, you have the course infor. Choose next action!")
        elif cd == 'i3':
            try:
                mark_sheet = input_mark(list_students, list_courses)
                print("Now, you have the marksheet. Choose next action!")
            except:
                print("Have you entered the list students or list courses yet?")
        elif cd == 's1':
            try:
                show_students(list_students)
            except:
                print("Do not have students list!")  
        elif cd == 's2':
            try:
                show_course(list_courses)
            except:
                print("Do not have course list!")

        elif cd == 's3':
            try:
                show_mark(mark_sheet)
            except:
                print("Do not have the mark sheet!")
        elif cd == 'e':
            break
        else:
            print("That's command not exist")

main()





