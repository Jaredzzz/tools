import os
import numpy as np
import shutil


def pick_from_name(pickpath,savepath,key_name_list):
    for filename in os.listdir(pickpath):
        filepath = os.path.join(pickpath,filename)
        for key_name in key_name_list:
            if key_name in filename:
                shutil.copy(filepath, os.path.join(savepath,key_name))
            else:
                pass


if __name__ == '__main__':
    pickpath = "NEU-CLS"
    savepath = "NEU"
    key_name_list = ["Cr", "In", "Pa", "PS", "RS", "SC"]
    if os.path.exists(savepath):
        for root, dirs, files in os.walk(savepath, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))
        os.mkdir(savepath)
    else:
        os.mkdir(savepath)
    pick_from_name(pickpath=pickpath,savepath=savepath,key_name_list=key_name_list)



