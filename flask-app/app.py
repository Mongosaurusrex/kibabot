from flask import Flask
from flask_bcrypt import Bcrypt
from flask_restful import Api
from datetime import datetime
from database.db import initialize_db
from resources.routes import initialize_routes
from utils.settings import MONGODB_CONNECTION_STRING

app = Flask(__name__)
api = Api(app)
bcrypt = Bcrypt(app)

app.config['JSON_AS_ASCII'] = False
app.config['MONGODB_SETTINGS'] = {
    'host': MONGODB_CONNECTION_STRING
}

initialize_db(app)
initialize_routes(api)

app.run(port=3000)
