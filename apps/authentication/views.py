from flask import Blueprint, json,request
import jwt
from common.decorators import token_required
from datetime import datetime, timedelta
from datetime import timezone
from flask.views import MethodView
from environ import SECRET_KEY

authprint = Blueprint('authprint',__name__,url_prefix='/api')

# @authprint.route('/token/', methods = ['GET'])
class AuthToken(MethodView):


    def get(self):
        token = jwt.encode(payload={'exp':datetime.now(tz=timezone.utc)+timedelta(minutes=10),'iat':datetime.now(tz=timezone.utc)},algorithm="HS256",key=SECRET_KEY)
        return json.jsonify(access_token = token),201

    def post(self):
        data = request.get_json()
        token =  data.get('token', None)
        if  token =="" or None:  
            return json.jsonify(data='Token is invalid!')
        try:
            decodetoken = jwt.decode(jwt=token, algorithms="HS256", key=SECRET_KEY)
        except jwt.exceptions.ExpiredSignatureError:
            return json.jsonify(error = "Token is expired!")
        else: 
            return json.jsonify(token=token, status="verified"),200
        
