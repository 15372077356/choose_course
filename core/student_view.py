from interface import student_interface,common_interface
from lib import common

user_info = {'username':None}

def register():
    print('欢迎注册')
    while True:
        username = input('请输入用户名>>>').strip()
        pwd = input('请输入密码>>>').strip()
        pwd2 = input('请再次输入密码>>>').strip()

        if pwd ==pwd2:
            flag,msg = student_interface.register_interface(username,pwd)
            if flag:
                print(msg)
                break
            else:
                print(msg)
                continue
        else:
            print('两次输入密码不一致')
            continue

def login():
    print('欢迎登录')
    while True:
        username = input('请输入用户名>>>').strip()
        pwd = input('请输入密码>>>').strip()

        flag, msg = common_interface.login_interface(username, pwd, 'student')
        if flag:
            user_info['username'] = username
            print(msg)
            break
        else:
            print(msg)

@common.login_auth('student')
def choose_school():
    print('欢迎选择学校')
    while True:
        username = user_info['username']
        school_list = common_interface.get_list_interface('school')

        if not school_list:
            print('还未创建学校')
            continue

        for i, school in enumerate(school_list):
            print(i, school)

        choice = input('请选择你需要创建课程的学校编号>>>').strip()

        if choice == 'q':
            break

        if not choice.isdigit():
            print('请输入数字')
            continue

        choice = int(choice)

        if choice not in range(len(school_list)):
            print('输入错误')
            continue

        school_name = school_list[choice]
        flag,msg = student_interface.choose_school_interface(username,school_name)
        if flag:
            print(msg)
            break
        else:
            print(msg)

@common.login_auth('student')
def choose_course():
    print('欢迎选择课程')

    while True:
        username = user_info['username']
        flag,course_list = student_interface.get_course_list_interface(username)
        if not flag:
            print(course_list)
            continue

        for i,course in enumerate(course_list):
            print(i,course)

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

        flag,msg = student_interface.choose_course_interface(username,course_name)
        if flag:
            print(msg)
            break
        else:
            print(msg)


@common.login_auth('student')
def check_score():
    print('欢迎查看成绩')
    username = user_info['username']
    score = student_interface.check_score_interface(username)
    if not score:
        print('暂无成绩')
    else:
        print(score)



def run():
    func_dic = {
        '1': register,
        '2': login,
        '3': choose_school,
        '4': choose_course,
        '5': check_score,
    }
    while True:
        print('''
        1.注册
        2.登录
        3.选择学校
        4.选择课程
        5.查看成绩
        q.退出

        ''')

        func_choice = input('请选择你需要的功能,输入q退出>>>')

        if func_choice == 'q':
            break

        if func_choice not in func_dic:
            print('输入错误')
            continue
        func_dic[func_choice]()