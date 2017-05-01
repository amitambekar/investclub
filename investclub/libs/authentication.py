import jwt
import json
from libs.helpers import mysql_connect,mysql_commit
from libs.helpers import setExceptionResponse,setResponse
import hashlib
import datetime
from investclub import settings
from django.contrib.sessions.models import Session
def	userLogin(request,username=None,password=None):
	try:
		if(check_auth(request,username,password)):
			auth_data = {}
			auth_data["usr"] = username
			auth_data['exp'] = datetime.datetime.utcnow() + datetime.timedelta(days=1)
			token = jwt.encode(auth_data, settings.SECRET_KEY, algorithm='HS256')
			request.session['auth_token'] = token
			request.session['username'] = username
			return setResponse({"message":"success","auth_token":token})
		else:
			return setExceptionResponse({"user_message":"Username and Password not matching","dev_message":"Username and Password not matching"})
	except Exception,e:
		print(e)
		return setExceptionResponse({"status":"message"})

def check_auth(request,username,password):
	password = hashlib.md5(password.encode('utf-8')).hexdigest()
	login_query = 'SELECT * FROM users WHERE username=\''+username+'\' and password=\''+password+'\''
	data = mysql_connect(login_query,'one')
	
	if len(data) > 0 and data["password"]==password and data["username"]==username and data['status'] == 'active' :
		return True
	else:
		return False