from flask import Flask
from flask.ext.script import Manager, Server

from elasticsearch import Elasticsearch
from flask.ext.mongoengine import MongoEngine
from pymongo import read_preferences
from celery import Celery

from datetime import datetime


app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {'DB': "employee", 'read_preference': read_preferences.ReadPreference.PRIMARY}
app.config["SECRET_KEY"] = "KeepThisS3cr3t"

app.config['CELERY_BROKER_URL'] = 'amqp://guest:guest@localhost:5672//'
app.config['CELERY_RESULT_BACKEND'] = 'amqp://'
app.config['CELERY_RESULT_BACKEND'] = 'mongodb://localhost:27017/'
app.config['CELERY_MONGODB_BACKEND_SETTINGS'] = {
    'database': 'db',
    'taskmeta_collection': 'employee',
}


def make_celery(app):
    celery = Celery('tasks', broker=app.config['CELERY_BROKER_URL'])
    celery.conf.update(app.config)
    TaskBase = celery.Task
    class ContextTask(TaskBase):
        abstract = True
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)
    celery.Task = ContextTask
    return celery

celery = make_celery(app)

manager = Manager(app)
manager.add_command("runserver", Server(
    use_debugger = True,
    use_reloader = True,
    host = '127.0.0.1')
)

db = MongoEngine(app)
es = Elasticsearch()

index = 'names'
_type = 'python_employees'
    
from test_app import views

@celery.task(name="tasks.add")
def add_random_names_elastic():
    names = [('Navaneethan', 'Python'), ('Siva', 'Erlang'), ('Karthick', 'C#'), ('Jagadesh', 'Django')]

    es.indices.create(index=index, ignore=400)
    for idx, item in enumerate(names):
        es.index(index=index, doc_type=_type, id=idx, body={"name": item[0], "timestamp": datetime.now(), "Job": item[1]})
        
    
if __name__ == '__main__':
    #add_random_names_elastic()
    app.run(debug=True, host="127.0.0.1")
