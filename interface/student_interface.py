from db import model

def register_interface(username,pwd):
    student_obj = model.Student.read(username)
    if student_obj:
        return False,'用户已存在'

    model.Student(username,pwd)
    return True,f'{username}注册成功'

def choose_school_interface(username,school_name):
    student_obj = model.Student.read(username)
    if student_obj.school:
        return False,'你已选择过学校'
    student_obj.add_school(school_name)
    return True,f'{username}选择学校{school_name}成功'

def get_course_list_interface(username):
    student_obj = model.Student.read(username)
    if not student_obj.school:
        return False,'请先选择学校'

    school_name = student_obj.school
    school_obj = model.School.read(school_name)
    return True,school_obj.course_list

def choose_course_interface(username,course_name):
    student_obj = model.Student.read(username)
    if course_name in student_obj.course_list:
        return False,'课程已选择'

    course_obj = model.Course.read(course_name)
    course_obj.add_student(username)
    student_obj.add_course(course_name)
    return True,f'{username}加入{course_name}成功'

def check_score_interface(username):
    student_obj = model.Student.read(username)
    return student_obj.score