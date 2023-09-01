from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

db_username = 'root'
db_password = 'qwer1234!'
db_host = 'localhost:3307'
db_name = 'blog'

connection_url = f"mysql://{db_username}:{db_password}@{db_host}/{db_name}"


app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'


app.config['SQLALCHEMY_DATABASE_URI'] = connection_url

db = SQLAlchemy(app)
app.app_context().push()
bcrypt = Bcrypt(app)
db.create_all()
login_manager = LoginManager(app)
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from flaskblog import routes