# Author: Rushikesh Nalla
# Date: 21st July, 2017

import numpy as np
import os
import csv
from sklearn.model_selection import train_test_split, cross_val_score, StratifiedKFold, GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler,MinMaxScaler
from joblib import Parallel, delayed
import multiprocessing
import statistics
import matplotlib.pyplot as plt

def machine(k, temp1, temp2):
    #X_train, X_test, y_train, y_test = train_test_split(temp1, temp2, test_size=0.1, random_state=14, stratify=temp2)
    #X_train = [[float(j) for j in i] for i in X_train]
    #X_test = [[float(j) for j in i] for i in X_test]
    #y_train = [int(i) for i in y_train]
    #y_test = [int(i) for i in y_test]
    #y_train = np.ravel(y_train)
    #y_test = np.ravel(y_test)

    #parameters = {'n_neighbors': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]}
    neigh = KNeighborsClassifier(n_neighbors=5, weights='distance', algorithm='auto')
    #grid = GridSearchCV(neigh, parameters)
    cv = StratifiedKFold(n_splits=10)
    scores = cross_val_score(neigh, temp1, temp2, cv=cv)
    #print(scores)
    print(statistics.mean(scores))
    #print(grid.get_params())
    mean = statistics.mean(scores)
    std = statistics.stdev(scores)
    left = mean - 1.96*(std/10**(1/2.0))
    right = mean + 1.96*(std/10**(1/2.0))
    plt.figure()
    plt.axvline(mean*100, color="blue", ymax=0.75, label='Mean Accuracy')
    plt.axvline(left*100, color="red", ymax= 0.5, label='95% Confidence Interval')
    plt.axvline(right*100, color="red", ymax=0.5)
    plt.text(50, 0.8, ' Mean Accuracy = %0.2f%% \n Lower limit of CI = %0.2f%% \n Upper Limit of CI = %0.2f%%' %(mean*100, left*100, right*100), fontsize=12)
    plt.xlim([50, 100])
    plt.legend(fontsize=11)
    plt.xlabel('Accuracy (in %)', fontsize=12)
    plt.title('Mean Accuracy and Confidence Interval \n K-Nearest Neighbors')
    plt.show()
    #neigh.fit(X_train, y_train)
    # y_pred = neigh.predict(X_test)
    # print(accuracy_score(y_test,y_pred))
    # print(neigh.score(X_test,y_test))
    #accuracy = neigh.score(X_test, y_test)
    #print(accuracy, k)
    #return accuracy

if __name__ == '__main__':
    dataPath = "LabelledData/"
    with open(os.path.join(dataPath, "AllData_in_One_File_14FGs_250_pts_each.csv"), 'rt') as csvfile:
        reader = csv.reader(csvfile)
        temp1 = []
        temp2 = []
        next(reader, None)
        for row in reader:
            temp1.append(row[2:])
            temp2.append(row[1])

    temp1 = StandardScaler().fit_transform(temp1)
    #temp1 = MinMaxScaler(feature_range=(0,1)).fit_transform(temp1)
    niter = 1
    ans = 0.
    inputs = range(niter)
    num_cores = multiprocessing.cpu_count()
    ans = Parallel(n_jobs=num_cores)(delayed(machine)(l, temp1, temp2) for l in inputs)
    #print(statistics.mean(ans))
    #print(statistics.stdev(ans))
    #plt.hist(ans, normed=True, bins=30)
    #plt.xlabel('Accuracy')
    #plt.show()
