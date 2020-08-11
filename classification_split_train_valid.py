import os
import random
import shutil


val_percent = 0.2
train_percent = 0.7
test_percent = 0.1
key_name_list = ["Cr", "In", "Pa", "PS", "RS", "Sc"]
data_savepath = "NEU"
for key_name in key_name_list:
    for type in ["train","test","valid"]:
      if os.path.exists(os.path.join(data_savepath, type,key_name)):
        for root, dirs, files in os.walk(os.path.join(data_savepath,type,key_name), topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))
      else:
        os.mkdir(os.path.join(data_savepath,type,key_name))
    key_image_path = os.path.join(data_savepath, key_name)
    total_key_image = os.listdir(key_image_path)

    num = len(total_key_image)
    print("all_num: %s" % num)
    # list = range(num)
    random.shuffle(total_key_image)
    valid = int(num * val_percent)  # val
    test = int(num * test_percent)  # test
    count = 0
    for image in total_key_image:
        image_path = os.path.join(key_image_path,image)
        if count < valid:
            shutil.copy(image_path , os.path.join(data_savepath,"valid",key_name))
        elif valid <= count < valid+test:
            shutil.copy(image_path, os.path.join(data_savepath, "test", key_name))
        else:
            shutil.copy(image_path, os.path.join(data_savepath, "train", key_name))
        count+=1

