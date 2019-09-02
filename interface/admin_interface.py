from db import model

def register_interface(username,pwd):
    admin_obj = model.Admin.read(username)
    if admin_obj:
        return False,'用户已存在'
    model.Admin(username,pwd)
    return True,f'{username}注册成功'

def create_school(username,school_name,school_addr):
    school_obj  = model.School.read(school_name)
    if school_obj:
        return False,'学校已存在'

    admin_obj = model.Admin.read(username)
    admin_obj.create_school(school_name,school_addr)
    return True,f'{school_name}学校创建成功'


def create_teacher(username,teacher_name,teacher_pwd = '123'):
    teacher_obj = model.Teacher.read(teacher_name)
    if teacher_obj:
        return False,'老师已创建'

    admin_obj = model.Admin.read(username)
    admin_obj.create_teacher(teacher_name, teacher_pwd)
    return True,f'{teacher_name}创建成功'

def create_course(username,school_name,course_name):
    course_obj = model.Course.read(course_name)
    if course_obj:
        return False,'课程已存在'

    admin_obj = model.Admin.read(username)
    admin_obj.create_course(school_name,course_name)
    return True,f'{course_name}创建成功'


