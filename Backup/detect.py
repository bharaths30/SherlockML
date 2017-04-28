#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      sbhar
#
# Created:     09/04/2017
# Copyright:   (c) sbhar 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#import numpy
import sys
print sys.path
import scipy
from sklearn import svm
from sklearn.externals import joblib
import mail_alert
trainingParamPath = "/home/ubuntu/sherlock/training_parameters/svm_hyperplane.txt"

#1st argument - filename containing 300(+1) lines of csv file collected for 5 mins
#2nd argument - deviceId from which the data was collected
#3rd argument - Emergency Email ID to which alert has to be sent
#4th argument - First name of the person whose phone is potentially lost
#5th,6th and 7th argument - Latitude , Longitude and name of the city obtained from the last known GPS location

def getTestData(filename):
    f_train=open(filename,"r")
    lines=f_train.readlines()
    i=0
    lines=lines[1:]
    noOfRows= len(lines)
    sequenceID=-1
    testDataList=[]
    currentRow=[]
    while(i<noOfRows):
        line=lines[i]
        line=line[:len(line)-1]
        tokens=line.split(',')
        label=tokens[len(tokens)-1]
        if label==sequenceID and len(currentRow)!=900:
            currentRow.extend(tokens[1:len(tokens)-1])
        else:
            if len(currentRow)==900:
                testDataList.append(currentRow)
            sequenceID=label
            currentRow=tokens[1:len(tokens)-1]
        i+=1
    if len(currentRow)==900:
        testDataList.append(currentRow)
    f_train.close()
    return testDataList

def detect(testDataSet,deviceId,emergencyEmail,firstname,latitude,longitude,cityName):
    clf = joblib.load(trainingParamPath)
    predictedData = (clf.predict(testDataSet))
    #f=open('/home/ubuntu/sherlock/result.txt','w')
    if predictedData[0]==deviceId:
	   print predictedData[0]
	   #f.write("false,"+predictedData[0]+","+deviceId)
    else:
	   print predictedData[0]
	   mail_alert.sendMail(emergencyEmail,firstname,latitude,longitude,cityName)
	   #f.write("true,"+predictedData[0]+","+deviceId)
    #f.close()
def main():
    #filename = sys.argv[1]
    testDataSetStr = sys.argv[1]
    oneDataPointTokens=testDataSetStr.split(",")
    testDataSet=[[]]
    for each in oneDataPointTokens:
	testDataSet[0].append(float(each))
    deviceId = sys.argv[2]
    emergencyEmail = sys.argv[3]
    firstname = sys.argv[4]
    latitude = sys.argv[5]
    longitude = sys.argv[6]
    cityName = sys.argv[7]
    #testDataSet=getTestData(filename)[:1]
    detect(testDataSet,deviceId,emergencyEmail,firstname,latitude,longitude,cityName)

if __name__ == '__main__':
    main()
