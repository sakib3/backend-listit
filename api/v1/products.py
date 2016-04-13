from . import api
from .. models import Product
from .. helpers import *
from flask import request
from mongoengine import ValidationError,NotUniqueError

#get products
@api.route('/products/', methods=['GET'])
def get_products():
	return Product.objects().get_all()

#create new product
@api.route('/products/', methods=['POST'])
def new_product():
	json_data = request.get_json()
	  
	if json_data is None:
		status_code = 400
		error = 'Bad Request'
		message = 'No content found'
		return send_error(error, message, status_code )

	else:
		#A mongoengine document object can be initialised with **kwargs
		try:
			new_product = Product(**json_data)
			new_product.save()
			message = 'Product is created'
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