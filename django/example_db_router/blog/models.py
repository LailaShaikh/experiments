from django.db import models

# Create your models here.

class EntryQuerySet(models.Manager):
    def published(self):
        return self.filter(publish=True)


class Entry(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    slug = models.SlugField(max_length=200, unique=True)
    publish = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    #objects = EntryQuerySet()

    def __unicode__(self):
        return "<Entry:%s>" %self.title
