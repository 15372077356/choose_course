

def login_auth(classify):
    from core import admin_view,student_view,teacher_view
    def outer(func):
        def inner(*args,**kwargs):
            if classify == 'admin':
                if admin_view.user_info.get('username'):
                    res= func(*args,**kwargs)
                    return res
                else:
                    print('请先登录')
                    admin_view.login()

            elif classify == 'student':
                if student_view.user_info.get('username'):
                    res= func(*args,**kwargs)
                    return res
                else:
                    print('请先登录')
                    student_view.login()

            elif classify == 'teacher':
                if teacher_view.user_info.get('username'):
                    res= func(*args,**kwargs)
                    return res
                else:
                    print('请先登录')
                    teacher_view.login()
        return inner
    return outer