import pickle
import os
from conf import settings

def save(obj):
    path = os.path.join(settings.DB_PATH,obj.__class__.__name__.lower())
    if not os.path.exists(path):
        os.mkdir(path)

    filename = os.path.join(path,obj.name)
    with open(filename,'wb') as fw:
        pickle.dump(obj,fw)

def read(classify,name):
    path = os.path.join(settings.DB_PATH,classify,name)
    if os.path.exists(path):
        with open(path,'rb') as fr:
            obj = pickle.load(fr)
            return obj


