from django.http import HttpResponse
import MySQLdb
from libs import config
import json
def mysql_connect(query,fetch='all'):
	connection=MySQLdb.connect(host=config.mysql_ip,user=config.mysql_login,passwd=config.mysql_pwd,db=config.mysql_db,port=int(config.mysql_port))
	cur=connection.cursor()
	cur.execute(query)
	result = [] 
	columns = tuple( [d[0].decode('utf8') for d in cur.description] ) 
	for row in cur:
		result.append(dict(zip(columns, row)))
	if fetch == 'one':
		if len(result) > 0:
			result = result[0]
	return result

def mysql_commit():
	connection.commit()

def setResponse(result):
	return HttpResponse(json.dumps(result))

def setExceptionResponse(result):
	return HttpResponse(json.dumps(result),status=500)
