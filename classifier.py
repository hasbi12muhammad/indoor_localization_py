import pandas
import matplotlib.pyplot as plt
from warnings import simplefilter
from pandas.plotting import scatter_matrix
from sklearn import model_selection
from sklearn.utils import shuffle
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

url_dt = "rssi_collected.csv"
url_ds = "rssi_data_test.csv"

header_dt, header_ds = ['ruang', 'time', 'sensor1', 'sensor2','sensor3','sensor4','sensor5'], [
    'ruang', 'time', 'sensor1', 'sensor2','sensor3','sensor4','sensor5']

data_training = pandas.read_csv(url_dt, names=header_dt)
data_set = pandas.read_csv(url_ds, names=header_ds)

del data_training['time']
del data_set['time']

# data_training.plot(kind='box', subplots=True, layout=(5,5), sharex=False, sharey=False)
# data_training.hist()
# scatter_matrix(data_training)
 
# plt.show()

arr = data_training.values
arr2 = data_set.values

arr = shuffle(arr, random_state=8)
arr2 = shuffle(arr2, random_state=8)

x_dt = arr[:, 1:6]
y_dt = arr[:, 0]

x_ds = arr2[:, 1:6]
y_ds = arr2[:, 0]

# ignore all future warnings
simplefilter(action='ignore', category=FutureWarning)

models = []

models.append(('LR', LogisticRegression()))

models.append(('LDA', LinearDiscriminantAnalysis()))

models.append(('KNN', KNeighborsClassifier()))

models.append(('CART', DecisionTreeClassifier()))

models.append(('NB', GaussianNB()))

models.append(('SVM', SVC()))

scoring = 'accuracy'
# evaluate each model in turn

results = []

names = []

for name, model in models:

    kfold = model_selection.KFold(n_splits=10)

    cv_results = model_selection.cross_val_score(
        model, x_dt, y_dt, cv=kfold, scoring='accuracy')

    results.append(cv_results)

    names.append(name)

    msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())

    print(msg)

# fig = plt.figure()
# fig.suptitle('Algorithm Comparison')
# ax = fig.add_subplot(111)
# plt.boxplot(results)
# ax.set_xticklabels(names)
# plt.show()

knn = KNeighborsClassifier()
knn.fit(x_dt, y_dt)
predictions = knn.predict(x_ds)

print()
print("predictions result :")
print("accuracy score : ",accuracy_score(y_ds, predictions))
print("confusion matrix : ")
print(confusion_matrix(y_ds, predictions))
print()
print("classification report : ")
print(classification_report(y_ds, predictions))
