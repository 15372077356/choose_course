from interface import teacher_interface,common_interface
from lib import common

user_info = {'username':None}

def login():
    print('欢迎登录')
    while True:
        username = input('请输入用户名>>>').strip()
        pwd = input('请输入密码>>>').strip()

        flag, msg = common_interface.login_interface(username, pwd, 'teacher')
        if flag:
            user_info['username'] = username
            print(msg)
            break
        else:
            print(msg)

@common.login_auth('teacher')
def check_course():
    print('欢迎查看课程')

    username =user_info['username']
    msg = teacher_interface.check_course_interface(username)
    if not msg:
        print('暂无课程')
    else:
        print(msg)

@common.login_auth('teacher')
def choose_course():
    print('欢迎选择课程')
    while True:
        username = user_info['username']
        course_list = common_interface.get_list_interface('course')

        for i, course in enumerate(course_list):
            print(i, course)

        choice = input('请选择你需要课程编号>>>').strip()

        if choice == 'q':
            break

        if not choice.isdigit():
            print('请输入数字')
            continue

        choice = int(choice)

        if choice not in range(len(course_list)):
            print('输入错误')
            continue

        course_name = course_list[choice]
        flag, msg = teacher_interface.choose_course_interface(username, course_name)
        if flag:
            print(msg)
            break
        else:
            print(msg)

@common.login_auth('teacher')
def check_student():
    print('欢迎查看学生')
    while True:
        teacher_name = user_info['username']
        course_list = teacher_interface.check_course_interface(teacher_name)

        if not course_list:
            print('请先增加课程')
            continue

        for i, course in enumerate(course_list):
            print(i, course)

        choice = input('请选择你需要的课程>>>').strip()

        if choice == 'q':
            break

        if not choice.isdigit():
            print('请输入数字')
            continue

        choice = int(choice)

        if choice not in range(len(course_list)):
            print('输入错误')
            continue
        course_name = course_list[choice]

        student_list = teacher_interface.check_student_interface(course_name)
        if not student_list:
            print('暂无学生')
        print(student_list)
        break

@common.login_auth('teacher')
def change_score():
    print('欢迎修改分数')
    while True:
        teacher_name = user_info['username']
        course_list = teacher_interface.check_course_interface(teacher_name)

        if not course_list:
            print('请先增加课程')
            continue

        for i, course in enumerate(course_list):
            print(i, course)

        choice = input('请选择你需要的课程>>>').strip()

        if choice == 'q':
            break

        if not choice.isdigit():
            print('请输入数字')
            continue

        choice = int(choice)

        if choice not in range(len(course_list)):
            print('输入错误')
            continue
        course_name = course_list[choice]

        student_list = teacher_interface.check_student_interface(course_name)

        for i,student in enumerate(student_list):
            print(i,student)

        choice2 = input('请选择学生编号>>>').strip()
        if choice2 == 'q':
            break

        if not choice2.isdigit():
            print('请输入数字')
            continue

        choice2 = int(choice2)

        if choice2 not in range(len(student_list)):
            print('输入错误')
            continue

        student_name = student_list[choice2]

        score = input('请输入你需要修改的分数>>>')

        msg = teacher_interface.change_score_interface(teacher_name,course_name,student_name,score)
        print(msg)
        break



def run():
    func_dic = {
        '1': login,
        '2': check_course,
        '3': choose_course,
        '4': check_student,
        '5': change_score,
    }
    while True:
        print('''
        1.登录
        2.查看教的课程
        3.选择教的课程
        4.查看课程学生
        5.修改学生成绩
        q.退出
        ''')

        choice = input('请选择老师功能:').strip()

        if choice == 'q':
            break

        if choice not in func_dic:
            print('选择有误!')
            continue

        func_dic.get(choice)()