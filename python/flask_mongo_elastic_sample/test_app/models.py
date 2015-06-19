from app import  db
from datetime import datetime

class Employee(db.Document):
    created_at = db.DateTimeField(default=datetime.now, required=True)
    name = db.StringField(max_length=255, required=True)
    job = db.StringField(max_length=255, required=True)
   
    def __unicode__(self):
        return self.name

    meta = {
        'allow_inheritance': True,
        'indexes': ['-created_at', 'name', 'job'],
        'ordering': ['-created_at']
    }
