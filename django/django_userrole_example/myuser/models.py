from django.db import models
from django.contrib.auth.models import User, Group, Permission


class Role(models.Model):
    name = models.CharField(max_length=50, unique=True, db_index=True)
    
    def __unicode__(self):
        return "%s" %self.name


class MyUser(models.Model):
    user = models.OneToOneField(User)
    address = models.TextField()
    roles = models.ManyToManyField(Role)

    def __unicode__(self):
        return '%s' % self.user

    def has_role(self, role):
        return role in [str(i.name)for i in self.roles.all()]
