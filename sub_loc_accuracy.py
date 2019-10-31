import pandas
from warnings import simplefilter



url_dt = "real_time_result_3_anchor.csv"

header_dt = ['predict','time','true_loc','sub_loc','compatiblity']

data = pandas.read_csv(url_dt, names=header_dt)

del data['time']

# arr = data.values
# arr = shuffle(arr, random_state=8)

sub_loc = ['A','B','C','D']
data_sub_loc_ruang1 = [[],[],[],[]]
data_sub_loc_ruang2 = [[],[],[],[]]
data_sub_loc_lorong = [[],[],[],[]]

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
            if item[i][2] == sub_loc[j]:
                data_sub_loc_lorong[j].append(item[i])
# ignore all future warnings
simplefilter(action='ignore', category=FutureWarning)

def mismatch_calc(arr):
    mismatch = [0,0,0,0]
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j][3] == "Mismatch":
                mismatch[i] = mismatch[i] + 1
    
    for i in range(len(arr)):
        percent = mismatch[i] / len(arr[i]) * 100
        print("             Sub-lokasi",arr[i][0][2], "=",percent,"%")


print("Kesalahan Prediksi pada Ruang 1 adalah :")
mismatch_calc(data_sub_loc_ruang1)
print("Kesalahan Prediksi pada Ruang 2 adalah :")
mismatch_calc(data_sub_loc_ruang2)
print("Kesalahan Prediksi pada Lorong adalah :")
mismatch_calc(data_sub_loc_lorong)


