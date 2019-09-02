from db import model

def check_course_interface(username):
    teacher_obj = model.Teacher.read(username)
    return teacher_obj.course_list

def choose_course_interface(username, course_name):
    teacher_obj = model.Teacher.read(username)
    if course_name in teacher_obj.course_list:
        return False,'课程已存在'

    teacher_obj.add_course(course_name)
    return True,f'{course_name}选择成功'

def check_student_interface(course_name):
    course_obj = model.Course.read(course_name)
    return course_obj.student_list

def change_score_interface(teacher_name,course_name,student_name,score):
    teacher_obj = model.Teacher.read(teacher_name)
    teacher_obj.change_score(course_name,student_name,score)
    return '修改成功'
