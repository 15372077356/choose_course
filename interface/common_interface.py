from db import db_handler
import os
from conf import settings

def login_interface(username, pwd,classify):
    obj = db_handler.read(classify,username)
    if not obj:
        return False,'用户不存在'
    if obj.pwd == pwd:
        return True,f'{username}登录成功'
    else:
        return False,'密码不正确'

def get_list_interface(classify):
    path = os.path.join(settings.DB_PATH,classify)
    if os.path.exists(path):
        return os.listdir(path)