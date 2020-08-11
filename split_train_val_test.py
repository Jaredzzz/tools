import os
import random

# trainval_percent = 0.1
train_percent = 0.8
xmlfilepath = 'Annotations'
txtsavepath = 'ImageSets\Main'
total_xml = os.listdir(xmlfilepath)

num = len(total_xml)
list = range(num)
num_train = int(num * train_percent)  # train
train = random.sample(list, num_train)

# ftrainval = open('ImageSets/Main/trainval.txt', 'w')
ftest = open('ImageSets/Main/test.txt', 'w')
ftrain = open('ImageSets/Main/train.txt', 'w')
fval = open('ImageSets/Main/val.txt', 'w')
count = 0
for i in list:
    name = total_xml[i][:-4] + '\n'
    if i in train:
        ftrain.write(name)

    else:
        if count%2==0:
            ftest.write(name)
        else:
            fval.write(name)
        count+=1
print("train:",num_train)
print("test + val :",count)
ftrain.close()
fval.close()
ftest.close()