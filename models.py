import os, json
from mongoengine import *
from flask import make_response

host = os.environ['MONGO_URI'] if 'MONGO_URI' in os.environ else 'mongodb://localhost:27017/listit'
db_name = os.environ['MONGO_DBNAME'] if 'MONGO_DBNAME' in os.environ else 'listit'

connect(db_name, host='mongodb://localhost:27017/listit')
class CustomQuerySet(QuerySet):

    def get_or_404(self):
        #detemine wheather query returned data
        query_result_found = False if len(self)==0 else True

        if query_result_found:
            return json.dumps(self.get().serialize())
        else:
            query_response =  make_response(json.dumps( {'error' : 'not found'} ), 404)
            return query_response


    def get_all(self):
        query_response = []
        results = self.all()
        for result in results:
            query_response.append(result.serialize())
        return json.dumps((query_response))


class Employee(Document):
    first_name = StringField()
    last_name = StringField()
    address = StringField()
    city_name = StringField()
    post_code = IntField()
    email = EmailField(unique=True, required=True)
    mobile = IntField()
    password = StringField(required=True)
    confirmed = BooleanField(default=False)
    meta = {'queryset_class': CustomQuerySet}

    def serialize(self):
        return {
            'id' : str(self.id),
            'first_name' : self.first_name,
            'last_name' : self.last_name,
            'address' : self.address,
            'city_name' : self.city_name,
            'post_code' : self.post_code,
            'email' : self.email,
            'mobile' : self.mobile,
            'password' : self.password,
            'confirmed' : self.confirmed
        }

    def clean(self):
            """Ensures that email, password is present and
            automatically sets the pub_date if published and not set"""
            if self.email is None or self.password is None:
                raise ValidationError
            
class Product(Document):
    name = StringField()
    family = StringField()

    def serialize(self):
        return {
            'id' : str(self.id),
            'name' : self.name,
            'family' : self.family
        }