# Author: Rushikesh Nalla
# Date: 21st July, 2017

from sklearn import svm
import os
import csv
from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score, GridSearchCV, permutation_test_score
from sklearn.metrics import confusion_matrix, accuracy_score
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from joblib import Parallel, delayed
import multiprocessing
import matplotlib.pyplot as plt
import statistics

def machine(k, temp1, temp2):
    #X_train, X_test, y_train, y_test = train_test_split(temp1, temp2, test_size=0.1, random_state=k, stratify=temp2)
    #X_train = [[float(j) for j in i] for i in X_train]
    #X_test = [[float(j) for j in i] for i in X_test]
    #y_train = [int(i) for i in y_train]
    #y_test = [int(i) for i in y_test]
    #y_train = np.ravel(y_train)
    #y_test = np.ravel(y_test)
    #X_train = np.array(X_train)
    #y_train = np.array(y_train)

    #parameters = {'kernel': ('linear', 'rbf', 'poly'), 'C': [1, 5, 10]}
    svr = svm.SVC(gamma='auto', kernel='rbf', C=10)
    #grid = GridSearchCV(svr, parameters)
    cv = StratifiedKFold(n_splits=10)
    scores = cross_val_score(svr, temp1, temp2, cv=cv)
    print(scores)
    #print(svr.get_params())
    #print(statistics.mean(scores))
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
    plt.title('Mean Accuracy and Confidence Interval \n Support Vector Machine')
    plt.show()

    #score, permutation_scores, p_value = permutation_test_score(grid, X_train, y_train,
    #                                                            scoring="accuracy", cv=cv, n_permutations=100, n_jobs=1)
    #print(score)
    #print(p_value)
    #plt.hist(permutation_scores, bins=10)
    #plt.xlabel('Score')
    #plt.show()
    #grid.fit(temp1, temp2)
    #print(grid.best_estimator_)
    #print(grid.best_params_)
    #print(grid.cv_results_)
    #predicted = grid.predict(X_test)
    #cnf_matrix = confusion_matrix(y_test, predicted)
    #print(cnf_matrix)
    #accuracy = accuracy_score(y_test, predicted)
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

