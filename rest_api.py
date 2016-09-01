from flask import Flask, request
import flask.ext.sqlalchemy
import flask.ext.restless


app = flask.Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///experiments.db'
db = flask.ext.sqlalchemy.SQLAlchemy(app)
db.drop_all()

# the rest api will show up under localhost:5000/api
# the class names below are used as the request api directory.  For example: if the class is Circ(db.Model) you can request the database at localhost:5000/api/circ

class Circ(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    sensor= db.Column(db.Integer, nullable=False)
    # datetime= db.Column(db.DateTime, nullable=True)


class Beeboxes(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    box= db.Column(db.Integer, nullable=False)
    correct= db.Column(db.Boolean, nullable=False)
    # datetime= db.Column(db.DateTime, nullable=True)
    
db.create_all()

manager = flask.ext.restless.APIManager(app, flask_sqlalchemy_db=db)
manager.create_api(Circ, methods= ['GET', 'POST', 'DELETE'], results_per_page=None)    
manager.create_api(Beeboxes, methods= ['GET', 'POST', 'DELETE'], results_per_page=None)    

app.run()
