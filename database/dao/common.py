from database.config import session
from datetime import datetime
import sqlite3

class GenericDAO:
    model = None   
    fields_to_json:list[str] = None

    def add(self,data:dict):
        obj = self.model()
        for i in data:
            setattr(obj, i,data[i])
        try:
            session.add(obj)
            session.commit()
        except Exception as e:
            return
        else:
            return self.tojson(obj=obj)

    def getall(self):
        data =  session.query(self.model).all()
        return data
    
    def get(self,id):
        data = session.query(self.model).get(id)
        return data
    
    def update(self,id,data:dict):
        obj = self.get(id=id)
        if obj is None:
            return False
        for i in data:
            setattr(obj,i,data[i])
        if hasattr(obj,'updated_on'):
            setattr(obj,"updated_on",datetime.now())
        try:
            session.commit()
        except Exception:
            return 
        return self.tojson(obj=obj)
    
    def delete(self, id):
        data = self.get(id=id)
        if data:
            session.delete(data)
            session.commit()
            return True
        return False
    
    def tojson(self,obj:object | list[object]):
        data = {i:getattr(obj,i) for i in self.fields_to_json}
        if 'created_on' in self.fields_to_json:
            data.update({'created_on':f"{data.get('created_on').date()} {data.get('created_on').time()}"})

        if 'updated_on' in self.fields_to_json:
            data.update({'updated_on':f"{data.get('updated_on').date()} {data.get('updated_on').time()}"})

        return data
    
    def tojsonall(self, obj:list[object]):
        result = []
        for i in obj:
            data = self.tojson(obj=i)
            result.append(data)
        return result