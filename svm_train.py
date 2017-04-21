# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 00:07:34 2017

@author: sbhar
"""

from sklearn import svm
from sklearn.externals import joblib
import os
from sklearn.model_selection import cross_val_score

basepath = "/home/ubuntu/ML-model/"

def getTrainingData():
    filename="sub_train.csv"
    f_train=open(filename,"r")
    lines=f_train.readlines()
    i=0
    lines=lines[1:]
    noOfRows= len(lines)
    trainingLabel=-1
    trainingFeatureList=[]
    trainingLabelList=[]
    currentRow=[]
    while(i<noOfRows):
        line=lines[i]
        line=line[:len(line)-1]
        tokens=line.split(',')
        label=tokens[len(tokens)-1]
	label = label[:len(label)-1]
	#print label, label[:len(label)-1]
        if label==trainingLabel and len(currentRow)!=900:
            currentRow.extend(tokens[1:len(tokens)-1])
        else:
            if len(currentRow)==900:
                trainingFeatureList.append(currentRow)
                trainingLabelList.append(trainingLabel)
            trainingLabel=label
            currentRow=tokens[1:len(tokens)-1]
        i+=1
    if len(currentRow)==900:
        trainingFeatureList.append(currentRow)
        trainingLabelList.append(trainingLabel)
    #print len(trainingLabelList), len(trainingFeatureList)
    #for each in trainingFeatureList:
    #   print len(each)
    f_train.close()
    return (trainingFeatureList,trainingLabelList)

def main():
    #X = [[0, 0], [1, 1]]
    #y = [0, 1]
    (trainingFeatures,labels)=getTrainingData()
    clf = svm.SVC()
    clf.fit(trainingFeatures, labels)
    scores = cross_val_score(clf, trainingFeatures, labels, cv=5)
    print scores
    testData=[]
    testData.append(trainingFeatures[0])
    print (clf.predict(testData))
    trainingParamPath = os.path.join(basepath,"Training_Parameters","svm_hyperplane.txt")
    print trainingParamPath
    joblib.dump(clf, trainingParamPath)

    #print (clf.predict([[2., 2.]]))

if __name__ == '__main__':
    main()
