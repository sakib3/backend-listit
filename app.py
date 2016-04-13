from flask import Flask
from flask.ext.cors import CORS
from api.v1 import api
from api.helpers import *

app = Flask(__name__)

app.register_blueprint(api,url_prefix='/api/v1')

CORS(app)
#home
@app.route('/', methods=['GET'])
def home():
  return send_response('Listit! :D')

@app.errorhandler(404)
def page_not_found(e):
    status_code = 404
    error = 'Not found'
    message = 'No content found'
    return send_error(error, message, status_code)

@app.errorhandler(400)
def page_not_found(e):
    status_code = 400
    error = 'Not found'
    message = 'No content found'
    return send_error(error, message, status_code)

if __name__ == '__main__':
    app.run(debug=True)
