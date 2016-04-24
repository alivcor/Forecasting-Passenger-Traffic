# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
from sklearn import datasets, linear_model
from sklearn import svm
from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures
import re
from sklearn.metrics import accuracy_score
from sklearn.pipeline import make_pipeline

months = list()
npgrs = list()
X_test=[61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72]


num = int(raw_input())
for i in range(1,num+1):
    mtuple=raw_input()
    s = mtuple.rstrip()
    objs = re.search(r'(\D+)(\d+)(\W+)(\d+)', s, re.M|re.I)
    months.append(int(objs.group(2)))
    npgrs.append(int(objs.group(4)))

    
clf=svm.SVR(kernel='rbf', C=1000, gamma=0.1)

    


X_m= np.array(months)
Y_n=np.array(npgrs)

X_m=X_m.reshape(X_m.shape[0], 1)


clf.fit(X_m, Y_n)

X_test = np.array(X_test)
X_test = X_test.reshape(X_test.shape[0], 1)
Y_pred=clf.predict(X_test)
for yps in Y_pred:
    print(int(yps))
