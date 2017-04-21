from flask import Flask
from flask import g
from flask import Response
from flask import request
import json
import MySQLdb

#import detect
detectModuleBasePath = "/home/ubuntu/sherlock/"
import os

app = Flask(__name__)

# CONNECTION ESTABLISHMENT FUNCTIONS
@app.before_request
def db_connect():
	g.conn = MySQLdb.connect(host='localhost',user='root',passwd='GroupTen',db='sherlock')
	g.cursor = g.conn.cursor()

@app.after_request
def db_disconnect(response):
	g.cursor.close()
	g.conn.close()
	return response

def userq(query, args=(), one=False):
	g.cursor.execute(query,args)
	rv = [dict((g.cursor.description[idx][0], value)
	for idx, value in enumerate(row)) for row in g.cursor.fetchall()]
	return (rv[0] if rv else None) if one else rv

# ROOT END-POINT
@app.route('/')
def hello_world():
  return 'Hello Master, Awaiting your instructions!'


# ACCOUNT REALTED END-POINTS

@app.route('/userauthlogin',methods=['POST'])
def usercheck():
	req_json = request.get_json()
	e_mail = str(req_json['email'])
	g.cursor.execute("SELECT password FROM users WHERE email LIKE %s",([e_mail]))
	# g.cursor.execute("SELECT password FROM users WHERE email='gvk@gmail.com'")
	try:
		value = g.cursor.fetchone()
		passwd = value[0]

		if (str(passwd) == str(req_json['password'])):
			userp = True
		else:
			userp = False
		result = {}
		result['userPresent'] = userp
		resp = Response(json.dumps(result),status=201,mimetype='application/json')
		return resp
	except:
		result['userPresent']=False
		resp = Response(json.dumps(result),status=201,mimetype='application/json')
		return resp

@app.route('/registeruserprofile',methods=['POST'])
def register():
	req_json = request.get_json()
	g.cursor.execute("SELECT COUNT(email) FROM users where email LIKE %s",([str(req_json['email'])]))
	g.conn.commit()
	value = g.cursor.fetchone()
	value = value[0]
	res = False
	print "Count reg value",value
	if (int(value) == 0):
		g.cursor.execute("INSERT INTO users(name,password,email,primarynumber,secondarynumber) VALUES (%s,%s,%s,%s,%s)",([str(req_json['name'])],[str(req_json['password'])],[str(req_json['email'])],[str(req_json['primaryPhone'])],[str(req_json['emergencyPhone'])]))
		g.conn.commit()
		res = True
	result = {}
	result['registerUserProfile'] = res
	resp = Response(json.dumps(result),status=202,mimetype='application/json')
	return resp


# TRAINING RELATED END-POINTS
@app.route('/datatraininginsert',methods=['POST'])
def traininginsert():
	req_json = request.get_json()
	print "Request",req_json
	dataPoint = req_json['oneDataPoint']
	print "Length",len(dataPoint)
	emailID = req_json['id']
	gpsLocation = req_json['gpsDataObject']
	countQuery = "SELECT COUNT(*) FROM training_done where userId=\""+emailID+"\";"
	g.cursor.execute(countQuery)
	result={}
	if g.cursor.fetchone()[0]==0:
		insertQuery = "INSERT INTO training(latitude,longitude,city"
    		for i in range(0,300):
    	   		insertQuery=insertQuery+",x"+str(i+1)+",y"+str(i+1)+",z"+str(i+1)
    		insertQuery=insertQuery+",id) VALUES ("
    		insertQuery = insertQuery + str(gpsLocation['latitude'])+","+str(gpsLocation['longitude']) +",\""+str(gpsLocation['cityName'])+"\""
    		for eachVal in dataPoint:
    	   		insertQuery = insertQuery +","+str(eachVal)
    		insertQuery = insertQuery +",\""+emailID+"\");"
    		g.cursor.execute(insertQuery)
    		g.conn.commit()
    		result['insertSuccess']=True
    		result['trainingComplete']=False
    		#result['anomaly']=False
    	else:
        	#testDataSet=[]
        	#testDataSet.append(dataPoint[:2])
		testDataSetStr=str(dataPoint[0])
		for each in dataPoint[1:]:
			testDataSetStr=testDataSetStr+","+str(each)
		#print "TestData is:"+str(testDataSet)
        	selectNameQuery="SELECT name FROM users WHERE email=\""+emailID+"\";"
        	g.cursor.execute(selectNameQuery)
        	name = g.cursor.fetchone()[0]
		resultPath = detectModuleBasePath+"/result.txt"
        	#boolAnomoly=detect.detect(testDataSet,emailID,emailID,name,gpsLocation['latitude'],gpsLocation['longitude'],gpsLocation['cityName'])
		executeDetect = "python "+detectModuleBasePath+"/detect.py "+str(testDataSetStr)+" "+str(emailID)+" "+str(emailID)+" "+str(name)+" "+str(gpsLocation['latitude'])+" "+str(gpsLocation['longitude'])+" "+str(gpsLocation['cityName'])#+" > "+detectModuleBasePath+"/result.txt"
		print executeDetect,resultPath
		os.system(executeDetect)
		"""if os.path.exists(resultPath):
			f=open(detectModuleBasePath+'/result.txt','r')
			data=f.read()
			if data.startswith('true'):
				result['anomaly']=True
			else:
				result['anomaly']=False
		else:
			result['anomaly']=False"""	
	       	result['insertSuccess']=False
        	result['trainingComplete']=True
        	#result['anomaly']=True
		f.close()
    	data = json.dumps(result)
    	resp = Response(data,status=200,mimetype='application/json')
    	return resp

#  DATA VIEW END-POINTS

@app.route('/data',methods=['GET'])
def show():
	result = userq("SELECT * FROM users")
	data = json.dumps(result)
	resp = Response(data,status=200,mimetype='application/json')
	return resp

@app.route('/trainingdata',methods=['GET'])
def trainingshow():
	result = userq("SELECT * FROM training")
	data = json.dumps(result)
        resp = Response(data,status=200,mimetype='application/json')
        return resp

# MAIN FUNCTION CALL
if __name__ == '__main__':
  app.run()
