#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      sbhar
#
# Created:     19/04/2017
# Copyright:   (c) sbhar 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import json
def main():
    f = open('testjson.json','r')
    p = json.load(f)
    l = p['oneDataPoint']
    d = p['GPSLocation']
    print type(d)

if __name__ == '__main__':
    main()
