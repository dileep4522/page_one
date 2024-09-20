from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:6304882347@192.168.29.185:5432/learning_db"
# app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:6304882347@192.168.0.129:5432/learning_db"
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
    'pool_pre_ping': True
}

db = SQLAlchemy(app)