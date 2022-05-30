# coding=utf-8

from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=64)
    author = models.CharField(max_length=64)
    pub_date = models.DateField()

    def __str__(self):
        return self.name + " " + self.author
