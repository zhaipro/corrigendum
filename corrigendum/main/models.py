# -*- coding: cp936 -*-
from django.db import models

# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=60, blank=True)
    state_province = models.CharField(max_length=30, blank=True)
    country = models.CharField(max_length=50, blank=True)
    website = models.URLField(blank=True, null=True)

    def __unicode__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40, blank=True)

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)


class Book(models.Model):
    title = models.CharField(max_length=200)
    authors = models.ManyToManyField(Author, related_name='author')
    translators = models.ManyToManyField(Author, related_name='translator', blank=True)
    ISBN = models.CharField(max_length=20, blank=True)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField(blank=True, null=True)
    
    def __unicode__(self):
        return self.title


class Corrigendum(models.Model):
    book = models.ForeignKey(Book)
    text = models.TextField()
    # 修改原因
    reason = models.CharField(max_length=200)
    create_date = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return self.text
