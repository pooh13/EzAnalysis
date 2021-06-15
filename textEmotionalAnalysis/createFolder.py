import platform
import time
import os

def createFolder(path):

    systemPlatform = ('windows', 'dos')

    if platform.system() == systemPlatform[0].capitalize() \
            or platform.system() == systemPlatform[0] \
            or platform.system() == systemPlatform[1].title() \
            or platform.system() == systemPlatform[1]:

        if path.find('/') == 0:
            path = path.replace('/', '\\')
        else:
            path = path
    else:
        if path.find('\\') == 0:
            path = path.replace('\\', '/')
        else:
            path = path

    localtime = time.strftime('%Y%m%d_%H%M%S',time.localtime(time.time()))

    if not os.path.exists(os.getcwd()+path+localtime):
        createdPath = os.getcwd()+path+localtime
        os.makedirs(createdPath, mode=0o777)
        print('Folder Create Finish！\nFolder PATH > "'+createdPath+'"')
    else:
        pass

    return createdPath
