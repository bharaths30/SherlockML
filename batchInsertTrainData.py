#from flask import g
import MySQLdb


def db_connect():
	conn = MySQLdb.connect(host='localhost',user='root',passwd='GroupTen',db='sherlock')
	cursor = conn.cursor()

def db_disconnect():
	cursor.close()
	conn.close()

def insertBatchTrainingData(filename):
    conn = MySQLdb.connect(host='localhost',user='root',passwd='GroupTen',db='sherlock')
    cursor = conn.cursor()
    f_train = open(filename, "r")
    lines = f_train.readlines()
    i = 0
    iter = 0
    linecount = 0
    lines = lines[1:]
    #singledatapoint = [33.388414, -111.931782, "Tempe"]
    first3Attrs= [33.388414, -111.931782, "Tempe"]
    emailID = 'joeljmj26@gmail.com'
    noOfRows = len(lines)
    count = noOfRows//300
    currentRow = []
    while(iter < count):
	singledatapoint=[]
	singledatapoint.append(first3Attrs[0])
	singledatapoint.append(first3Attrs[1])
	singledatapoint.append(first3Attrs[2])
	#singledatapoint=singledatapoint.extend(first3Attrs)
        while(i < 300):
            eachline = lines[linecount]
            eachline = eachline[:len(eachline)-1]
            tokens = eachline.split(',')
            tokens = tokens[1:]
            singledatapoint.extend(tokens)
            linecount+= 1
            i+= 1

        insertQuery = "INSERT INTO training(latitude,longitude,city"
        for i in range(0, 300):
            insertQuery = insertQuery + ",x" + str(i + 1) + ",y" + str(i + 1) + ",z" + str(i + 1)
        insertQuery = insertQuery + ",id) VALUES ("
        insertQuery = insertQuery + str(singledatapoint[0]) + "," + str(singledatapoint[1]) + ",\"" + str(singledatapoint[2]) + "\""
        for eachVal in range(3, 903):
            insertQuery = insertQuery + "," + str(singledatapoint[eachVal])
        insertQuery = insertQuery + ",\"" + emailID + "\");"
        #print insertQuery
        #vals = insertQuery.split("VALUES ")[1]
        #print len(vals.split(","))
        print iter
	cursor.execute(insertQuery)
        conn.commit()
        i = 0
        iter+= 1
    #db_disconnect()
    cursor.close()
    conn.close()



def main():
    filename = "accel_log.csv"
    insertBatchTrainingData(filename)


if __name__ == '__main__':
    main()
