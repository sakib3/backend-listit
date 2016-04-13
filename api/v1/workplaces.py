from . import api
from .. models import Workplace
from .. helpers import *
from flask import request
from mongoengine import ValidationError,NotUniqueError

#get workplaces
@api.route('/workplaces/', methods=['GET'])
def get_workplaces():
	return Workplace.objects().get_all()


#get the workplace
@api.route('/workplaces/<workplace_id>', methods=['GET'])
def get_the_workplace(workplace_id):
	try:
		return Workplace.objects(id=workplace_id).get_or_404()

	except (KeyError, ValidationError):
		status_code = 400
		error = 'ValidationError'
		message = 'Invalid Id'
		return send_error(error, message, status_code)

#create new workplace
@api.route('/workplaces/', methods=['POST'])
def new_workplace():
	json_data = request.get_json()
	  
	if json_data is None:
		status_code = 400
		error = 'Bad Request'
		message = 'No content found'
		return send_error(error, message, status_code )

	else:
		#A mongoengine document object can be initialised with **kwargs
		try:
			new_workplace = Workplace(**json_data)
			new_workplace.save()
			message = 'workplace is created'
			status_code = 201
			return send_response(message, status_code)
    

		except (KeyError, ValidationError):
			status_code = 400
			error = 'ValidationError'
			message = 'Name field is missing'
			return send_error(error, message, status_code)

		except (KeyError, NotUniqueError):
			status_code = 400
			error = 'NotUniqueError'
			message = 'Name already exist'
			return send_error(error, message, status_code)