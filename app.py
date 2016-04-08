import os, json
from flask import Flask, request
from bson import json_util
from bson.objectid import ObjectId
from flask.ext.pymongo import PyMongo

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ['SECRET_KEY'] if 'SECRET_KEY' in os.environ else 'this_should_be_configured'


#define MongoDB server configuration
app.config['MONGO_HOST'] = os.environ['MONGO_HOST'] if 'MONGO_HOST' in os.environ else 'localhost'
app.config['MONGO_PORT'] = os.environ['MONGO_PORT'] if 'MONGO_PORT' in os.environ else 27017
app.config['MONGO_DBNAME'] = os.environ['MONGO_DBNAME'] if 'MONGO_DBNAME' in os.environ else 'listit'
app.config['MONGO_USERNAME'] = os.environ['MONGO_USERNAME'] if 'MONGO_USERNAME' in os.environ else ''
app.config['MONGO_PASSWORD'] = os.environ['MONGO_PASSWORD'] if 'MONGO_PASSWORD' in os.environ else ''


# connect to MongoDB server
connection = PyMongo(app, config_prefix='MONGO')


#Convert Mongo object(s) to JSON
def toJson(data):
    return json.dumps(data, default=json_util.default)

#get all employees
@app.route('/employees/', methods=['GET'])
def employees():
  if request.method == 'GET':

    lim = int(request.args.get('limit', 10))
    off = int(request.args.get('offset', 0))
    results = connection.db.employee.find().skip(off).limit(lim)
    json_results = []

    for result in results:
      json_results.append(result)
    return toJson(json_results)

#get the employee
@app.route('/employees/<ObjectId:employee_id>', methods=['GET'])
def get_the_employee(employee_id):
  if request.method == 'GET':

    result = connection.db.employee.find_one_or_404(employee_id)
    return toJson(result)


#home
@app.route('/', methods=['GET'])
def home():
  return 'hello world'




if __name__ == '__main__':
    app.run(debug=True)
