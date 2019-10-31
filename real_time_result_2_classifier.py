import pandas
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

arr = data.values

arr = shuffle(arr, random_state=8)

predict_location = arr[:, 0]
true_location = arr[:, 1]

# ignore all future warnings
simplefilter(action='ignore', category=FutureWarning)


print()
print("predictions result :")
print("accuracy score : ",accuracy_score(true_location, predict_location))
print("confusion matrix : ")
print(confusion_matrix(true_location, predict_location))
print()
print("classification report : ")
print(classification_report(true_location, predict_location))
