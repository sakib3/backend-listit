import os, json, sys
from bson import json_util
from bson.objectid import ObjectId
from flask import Flask, request, jsonify
from models import *
from flask.ext.cors import CORS


app = Flask(__name__)
CORS(app)

def send_response(error, message, status_code):
      response = jsonify({'status': status_code, 'error': error,
                        'message': message})
      response.status_code = status_code
      return response

#Convert Mongo object(s) to JSON
def toJson(data):
    return json.dumps(data, default=json_util.default)


#home
@app.route('/', methods=['GET'])
def home():
  return 'hello world'



#get employees
@app.route('/employees/', methods=['GET'])
def employees():
  return Employee.objects().get_all()

#get the employee
@app.route('/employees/<employee_id>', methods=['GET'])
def get_the_employee(employee_id):
  return Employee.objects(id=employee_id).get_or_404()

@app.route('/employees/', methods=['POST'])
def new_employee():
  json_data = request.get_json()
  
  if json_data is None:
    return 'not found'
  #email = json_data['email']
  else:
    #A mongoengine document object can be initialised with **kwargs
    try:
      new_employee = Employee(**json_data)
      new_employee.save()
      return 'toJson(json_data)'
    

    except (KeyError, ValidationError):
      status_code = 400
      error = 'ValidationError'
      message = 'Email or Password field is missing'
      return send_response(error, message, status_code)

    except (KeyError, NotUniqueError):
      status_code = 400
      error = 'NotUniqueError'
      message = 'Email already exist'
      return send_response(error, message, status_code)



if __name__ == '__main__':
    app.run(debug=True)
