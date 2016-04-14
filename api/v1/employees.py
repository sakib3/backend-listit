from . import api
from .. models import Employee
from .. helpers import *
from flask import request
from mongoengine import ValidationError,NotUniqueError

#get employees
@api.route('/employees/', methods=['GET'])
def employees():
  return Employee.objects().get_all()


#get the employee
@api.route('/employees/<employee_id>', methods=['GET'])
def get_the_employee(employee_id):
 try:
  return Employee.objects(id=employee_id).get_or_404()
 except (KeyError, ValidationError):
  status_code = 400
  error = 'ValidationError'
  message = 'Invalid Id'
  return send_error(error, message, status_code)

@api.route('/employees/', methods=['POST'])
def new_employee():
  json_data = request.get_json()

  if json_data is None:
    status_code = 400
    error = 'Bad Request'
    message = 'No content found'
    return send_error(error, message, status_code)
  else:
    #A mongoengine document object can be initialised with **kwargs
    try:
      new_employee = Employee(**json_data)
      new_employee.save()
      message = 'Employee is created'
      status_code = 201
      return send_response(message, status_code)


    except (KeyError, ValidationError):
      status_code = 400
      error = 'ValidationError'
      message = 'Email or Password field is missing'
      return send_error(error, message, status_code)

    except (KeyError, NotUniqueError):
      status_code = 400
      error = 'NotUniqueError'
      message = 'Email already exist'
      return send_error(error, message, status_code)
