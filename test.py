from sklearn.utils import shuffle

X=[1,2,3]
y = ['one', 'two', 'three']
X, y = shuffle(X, y)
print(X)
print(y)