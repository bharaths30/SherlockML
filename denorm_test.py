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

def main():
    filename="sub_test.csv"
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
    #print len(testDataList)
    #for each in testDataList:
        #print each
    f_train.close()


if __name__ == '__main__':
    main()
