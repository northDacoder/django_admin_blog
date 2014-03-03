from django.contrib.auth.models import User
from django.db import models

# MODELS CREATED HERE #
class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    author = models.ForeignKey(User)
    posted = models.DateTimeField(auto_now=True)
    url = models.SlugField()

    def __unicode__(self):
        return self.title


class Comment(models.Model):
    name = models.CharField(max_length=20)
    comment = models.TextField()
    post = models.ForeignKey(BlogPost)

    def __unicode__(self):
        return self.name



