from flask import Flask
from flask.ext.cors import CORS
from api.v1 import api

app = Flask(__name__)

app.register_blueprint(api,url_prefix='/api/v1')

CORS(app)
#home
@app.route('/', methods=['GET'])
def home():
  return 'Listit! :D'

if __name__ == '__main__':
    app.run(debug=True)
