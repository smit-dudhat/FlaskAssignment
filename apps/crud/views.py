from flask import Blueprint, request, json, Request
from flask.views import MethodView
from common.decorators import token_required
from database.config import session
from database.models.book import Book
from database.dao.bookdao import bookdao
from datetime import datetime

crudprints = Blueprint('crudprints',__name__, url_prefix="/api")

class CrudOperations(MethodView):
    decorators = [token_required]

    def get(self, id=None):
        if id:
            book = bookdao.get(id=id)
            if book is None:
                return json.jsonify(data="Requested data is not found!"),404
            data = bookdao.tojson(book)
            return json.jsonify(data=data),200
        
        books = bookdao.getall()
        if books is not None:
            data = bookdao.tojsonall(obj=books)
            return json.jsonify(data=data),200
        return json.jsonify(data="No data found!"),404
    
    def post(self):
        data = request.json
        title = data.get('title')
        desc = data.get('description')
        if  (title == "" or None) or (desc == "" or None):
            return json.jsonify(error="title or desciption can not be blank"),400
        book = bookdao.add(data=data)
        if book is not None:
            return json.jsonify(data=book),201
        return json.jsonify(error="error occured in db operations"),201
    
    def delete(self,id):
        deleted = bookdao.delete(id=id)
        if not deleted:
            return json.jsonify(data="Requested data is not found!"),404
        return json.jsonify(result="Data deleted!"),200
    
    def patch(self,id):
        data = request.json
        updated = bookdao.update(id=id, data=data)
        if  not updated:
            return json.jsonify(data="Requested data is not found!"),404
        if updated is None:
            return json.jsonify(error="Error occured while updating data."),304
        return json.jsonify(result=updated),200

