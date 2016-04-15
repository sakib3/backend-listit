import os, json
from mongoengine import *
from flask import make_response
from . helpers import *
from werkzeug.security import generate_password_hash, check_password_hash

host = os.environ['MONGO_URI'] if 'MONGO_URI' in os.environ else 'mongodb://localhost:27017/listit'
db_name = os.environ['MONGO_DBNAME'] if 'MONGO_DBNAME' in os.environ else 'listit'

connect(db_name, host=host)
class CustomQuerySet(QuerySet):

    def get_or_404(self):
        #detemine wheather query returned data
        query_result_found = False if len(self)==0 else True

        if query_result_found:
            return json.dumps(self.get().serialize())
        else:
            status_code = 404
            error = 'Not found'
            message = 'No content found'
            return send_error(error, message, status_code)


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

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def verify_password(self, password):
        return check_password(self.password, password)

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
            """Ensures that email, password is present """
            if self.email is None or self.password is None:
                raise ValidationError
            self.password = generate_password_hash(self.password)

class Product(Document):
    name = StringField(required=True)
    family = StringField()
    meta = {'queryset_class': CustomQuerySet}

    def serialize(self):
        return {
            'id' : str(self.id),
            'name' : self.name,
            'family' : self.family
        }

    def clean(self):
            """Ensures that name is present """
            if self.name is None:
                raise ValidationError

class Workplace(Document):
    name = StringField(required=True)
    address = StringField(required=True)
    city_name = StringField(required=True)
    post_code = IntField(required=True)
    meta = {'queryset_class': CustomQuerySet}

    def serialize(self):
        return {
            'id' : str(self.id),
            'name' : self.name,
            'address' : self.address,
            'city_name' : self.city_name,
            'post_code' : self.post_code
        }

    def clean(self):
            """Ensures that name is present """
            if self.name is None or self.address is None or self.city_name is None or self.post_code is None:
                raise ValidationError
