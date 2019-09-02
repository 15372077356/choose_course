from core import admin_view,teacher_view,student_view

def run():
    func_dic = {
        '1': admin_view.run,
        '2': student_view.run,
        '3': teacher_view.run,
    }
    msg = '''
       1.管理员视图
       2.学生视图
       3.老师视图
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