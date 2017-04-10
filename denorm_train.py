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
import csv
def main():
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

if __name__ == '__main__':
    main()
