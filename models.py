__author__ = 'alsenis'


from django.contrib import admin
from django.db import models

class PostTag(models.Model):
    title = models.TextField(max_length=20)

admin.site.register(PostTag)

class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    timestamp = models.DateTimeField()
    author = models.ManyToManyField(PostTag)

    class Meta:
        ordering = ('-timestamp',)

admin.site.register(BlogPost)