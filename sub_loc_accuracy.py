import pandas
import numpy
import matplotlib.pyplot as plt
from warnings import simplefilter
from sklearn.utils import shuffle
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix

url_dt = "real_time_result_2.csv"

header_dt = ['predict','time','true_loc','sub_loc','compatiblity']

data = pandas.read_csv(url_dt, names=header_dt)

del data['time']

# arr = data.values
# arr = shuffle(arr, random_state=8)

sub_loc = ['A','B','C','D']
data_sub_loc_ruang1 = [[],[],[],[]]
data_sub_loc_ruang2 = [[],[],[],[]]
data_sub_loc_lorong = [[],[],[],[]]
data_true_loc = []

item = data.values
for i in range(len(data)):
    if item[i][1] == "Ruang 1":
        for j in range(4):
            if item[i][2] == sub_loc[j]:
                data_sub_loc_ruang1[j].append(item[i])
    elif item[i][1] == "Ruang 2":
        for j in range(4):
            if item[i][2] == sub_loc[j]:
                data_sub_loc_ruang2[j].append(item[i])
    else:
        for j in range(4):
            if item[j][2] == sub_loc[j]:
                data_sub_loc_lorong[j].append(item[i])
# ignore all future warnings
simplefilter(action='ignore', category=FutureWarning)

# def mismatch_calc(arr):
#     mismatch = o
#     for i in range(len(arr)):
#         for j in range(len(arr[i])):
#             if arr[i]
for i in range(len(data_sub_loc_ruang1)):
    for j in range(len(data_sub_loc_ruang1[i])):
        print(data_sub_loc_ruang1[i][j])
print()
for i in range(len(data_sub_loc_ruang2)):
    for j in range(len(data_sub_loc_ruang2[i])):
        print(data_sub_loc_ruang2[i][j])
print()
for i in range(len(data_sub_loc_lorong)):
    for j in range(len(data_sub_loc_lorong[i])):
        print(data_sub_loc_lorong[i][j])


