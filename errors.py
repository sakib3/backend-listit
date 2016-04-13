from app import app
from api.helpers import *

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