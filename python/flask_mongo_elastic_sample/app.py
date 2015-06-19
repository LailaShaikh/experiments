from flask import Flask
from flask.ext.script import Manager, Server

from elasticsearch import Elasticsearch
from flask.ext.mongoengine import MongoEngine
from pymongo import read_preferences

from datetime import datetime


app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {'DB': "employee", 'read_preference': read_preferences.ReadPreference.PRIMARY}
app.config["SECRET_KEY"] = "KeepThisS3cr3t"

manager = Manager(app)
manager.add_command("runserver", Server(
    use_debugger = True,
    use_reloader = True,
    host = '0.0.0.0')
)

db = MongoEngine(app)
es = Elasticsearch()

index = 'names'
_type = 'python_employees'
    
from test_app import views

def add_random_names_elastic():
    names = [('Navaneethan', 'Python'), ('Siva', 'Erlang'), ('Karthick', 'C#'), ('Jagadesh', 'Django')]

    es.indices.create(index=index, ignore=400)
    for idx, item in enumerate(names):
        es.index(index=index, doc_type=_type, id=idx, body={"name": item[0], "timestamp": datetime.now(), "Job": item[1]})
        
    
if __name__ == '__main__':
    #add_random_names_elastic()
    app.run(debug=True)
