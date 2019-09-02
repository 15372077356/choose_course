from interface import admin_interface,common_interface
from lib import common

user_info = {'username':None}
def register():
    print('欢迎注册')
    while True:
        username = input('请输入用户名>>>').strip()
        pwd = input('请输入密码>>>').strip()
        pwd2 = input('请再次输入密码>>>').strip()

        if pwd ==pwd2:
            flag,msg = admin_interface.register_interface(username,pwd)
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

        flag, msg = common_interface.login_interface(username, pwd,'admin')
        if flag:
            user_info['username'] = username
            print(msg)
            break
        else:
            print(msg)

@common.login_auth('admin')
def create_school():
    print('欢迎创建学校')

    while True:
        username = user_info['username']
        school_name = input('请输入学校名称>>>').strip()
        school_addr = input('请输入学校地址>>>').strip()

        flag,msg = admin_interface.create_school(username,school_name,school_addr)
        if flag:
            print(msg)
            break
        else:
            print(msg)

@common.login_auth('admin')
def create_teacher():
    print('欢迎创建老师')

    while True:
        username = user_info['username']
        teacher_name = input('请输入老师名字>>>').strip()

        flag,msg = admin_interface.create_teacher(username,teacher_name)
        if flag:
            print(msg)
            break
        else:
            print(msg)


@common.login_auth('admin')
def create_course():
    print('欢迎创建课程')
    while True:
        username = user_info['username']
        school_list = common_interface.get_list_interface('school')

        if not school_list:
            print('请先创建学校')
            continue

        for i,school in enumerate(school_list):
            print(i,school)

        choice = input('请选择你需要创建课程的学校编号>>>').strip()

        if choice =='q':
            break

        if not choice.isdigit():
            print('请输入数字')
            continue

        choice = int(choice)

        if choice not in range(len(school_list)):
            print('输入错误')
            continue

        school_name = school_list[choice]
        course_name = input('请输入课程名称>>>').strip()

        flag,msg = admin_interface.create_course(username,school_name,course_name)
        if flag:
            print(msg)
            break
        else:
            print(msg)



def run():
    func_dic = {
        '1': register,
        '2': login,
        '3': create_school,
        '4': create_teacher,
        '5': create_course,
    }
    msg = '''
              1.注册
              2.登录
              3.创建学校
              4.创建老师
              5.创建课程
              q.退出
              '''
    while True:
        print(msg)
        choice = input('请选择你需要的视图>>>').strip()

        if choice == 'q':
            break

        if not choice.isdigit():
            print('请重新输入')
            continue

        func_dic[choice]()