from flask import jsonify


def send_error(error, message, status_code):
  response = jsonify({'status': status_code, 'error': error,
                    'message': message})
  response.status_code = status_code
  return response

def send_response(message, status_code=200):
  response = jsonify({'status': status_code,'message': message})
  response.status_code = status_code
  return response

#Convert Mongo object(s) to JSON
def toJson(data):
  return json.dumps(data, default=json_util.default)