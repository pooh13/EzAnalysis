import platform
import time
import os

def createFolder(path):

    if platform.system() == systemPlatform[0] \
            or platform.system() == systemPlatform[1] \
            or platform.system() == systemPlatform[2] \
            or platform.system() == systemPlatform[3]:
        path = (r'\Models\MLP_Model\\')
    else:
        path = ('/Models/MLP_Model/')

    localtime = time.strftime('%Y%m%d_%H%M%S',time.localtime(time.time()))

    if not os.path.exists(os.getcwd()+path+localtime):
        createdPath = os.getcwd()+path+localtime
        os.makedirs(createdPath, mode=0o777)
        print('Folder Create Finish！')
    else:
        pass

    return createdPath
