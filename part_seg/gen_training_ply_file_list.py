
import string, sys
from numpy import *
from numpy.linalg import *
from os import listdir
from os.path import isfile, join

# read data
mainpath = "PartAnnotation"
lines = open(mainpath + "/synsetoffset2category.txt", "r").readlines()
results = []
categories = []
for l in lines:
    l = l.split("\t")
    # ['Airplane', '02691156\n']
    categories.append(l[1][0:len(l) - 3])
print("categories[0] = ", categories[0])

testing = []
lines = open("testing_ply_file_list.txt", "r").readlines()
for l in lines:
    testing.append(l[0:len(l) - 1])
print("testing[0] = ", testing[0])
print("testing files size = ", len(testing))

label_res = []
for cat in categories:
    # read all data under each categories
    # data_path = mainpath + "/" + cat + "/points"
    # data_res = []
    # data_files = [f for f in listdir(data_path) if isfile(join(data_path, f))]
    # print("data files size = ",len(data_files))
    # for filename in data_files:
    #     labelname = filename[0:-3] + "seg"
    #     data_path = cat + "/points/" + filename + " " + cat + "/expert_verified/points_label/" + labelname + " " + cat
    #     data_res.append(data_path)
    # print("data_res[0] = ", data_res[0])
    # read all label under each categories

    labe_path = mainpath + "/" + cat + "/expert_verified/points_label"
    label_files = [f for f in listdir(labe_path) if isfile(join(labe_path, f))]
    print("label files size = ",len(label_files))
    print("label_files[0] = ", label_files[0])
    for filename in label_files:
        dataname = filename[0:-3] + "pts"
        data_path = cat + "/points/" + dataname + " " + cat + "/expert_verified/points_label/" + filename + " " + cat
        label_res.append(data_path)

print("label_res[0] = ",label_res[0])

out_lines = []
for l in label_res:
    if l in testing :
        continue
    else:
        out_lines.append(l)
print("out_lines len = ", len(out_lines))
ofname = "training_ply_file_list.txt"
with open(ofname, mode='w') as fo:
        for l in out_lines:
            fo.write(str(l)+'\n')
