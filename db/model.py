from db import db_handler

class Base():
    def save(self):
        db_handler.save(self)
    @classmethod
    def read(cls,name):
        obj = db_handler.read(cls.__name__.lower(),name)
        return obj

class Admin(Base):
    def __init__(self,name,pwd):
        self.name =name
        self.pwd = pwd
        self.save()
    def create_school(self,school_name,school_addr):
        School(school_name,school_addr)

    def create_teacher(self,teacher_name,teacher_pwd):
        Teacher(teacher_name,teacher_pwd)

    def create_course(self,school_name,course_name):
        school_obj = School.read(school_name)
        school_obj.add_course(course_name)
        Course(course_name)

class School(Base):
    def __init__(self,school_name,school_addr):
        self.name= school_name
        self.addr = school_addr
        self.course_list = []
        self.save()
    def add_course(self,course_name):
        self.course_list.append(course_name)
        self.save()

class Teacher(Base):
    def __init__(self,teacher_name,teacher_pwd):
        self.name= teacher_name
        self.pwd = teacher_pwd
        self.course_list = []
        self.save()
    def add_course(self,course_name):
        self.course_list.append(course_name)
        self.save()

    def change_score(self,course_name,student_name,score):
        student_obj = Student.read(student_name)
        student_obj.change_score(course_name,score)

class Course(Base):
    def __init__(self,course_name):
        self.name= course_name
        self.student_list = []
        self.save()

    def add_student(self,student_name):
        self.student_list.append(student_name)
        self.save()

class Student(Base):
    def __init__(self,student_name,student_pwd):
        self.name = student_name
        self.pwd = student_pwd
        self.school = None
        self.course_list = []
        self.score = {}
        self.save()

    def add_course(self,course_name):
        self.course_list.append(course_name)
        self.score[course_name] = 0
        self.save()

    def add_school(self,school_name):
        self.school = school_name
        self.save()

    def change_score(self,course_name,score):
        self.score[course_name] = score
        self.save()

