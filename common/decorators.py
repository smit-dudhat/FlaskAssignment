import jwt
from flask import request, json
from environ import SECRET_KEY
from functools import wraps

def token_required(func):
    @wraps(func)
    def decoratred_func(*args,**kwargs):
        auth = request.authorization
        if auth is None:
            return json.jsonify(error='Token is not provided!'),401
        try:
            decode = jwt.decode(jwt=auth.token, algorithms="HS256", key=SECRET_KEY)
        except jwt.ExpiredSignatureError:
            return json.jsonify(error='Token is expired!'),401
        else:
            result = func(*args,**kwargs)
            return result
    return decoratred_func
