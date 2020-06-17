from django.db import models


# Create your models here.
class Student(models.Model):
    userid = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=200)
    username = models.CharField(max_length=200, null=True)
    logintime = models.CharField(max_length=200, null=True)
    jointime = models.CharField(max_length=200, null=True)


class Admin(models.Model):
    userid = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=200)
    username = models.CharField(max_length=200, null=True)
    logintime = models.CharField(max_length=200, null=True)
    jointime = models.CharField(max_length=200, null=True)


class Leader(models.Model):
    userid = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=200)
    username = models.CharField(max_length=200, null=True)
    logintime = models.CharField(max_length=200, null=True)
    jointime = models.CharField(max_length=200, null=True)
