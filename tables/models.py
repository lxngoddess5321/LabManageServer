from django.db import models


# Create your models here.
class Trs(models.Model):
    userid = models.CharField(max_length=50)
    data = models.CharField(max_length=5000)
    time = models.CharField(max_length=100)
    admin = models.CharField(max_length=400, null=True)
    leader = models.CharField(max_length=400, null=True)


class Plst(models.Model):
    userid = models.CharField(max_length=50)
    data = models.CharField(max_length=5000)
    time = models.CharField(max_length=100)


class Ravt(models.Model):
    userid = models.CharField(max_length=50)
    data = models.CharField(max_length=5000)
    time = models.CharField(max_length=100)


class Ucst(models.Model):
    userid = models.CharField(max_length=50)
    data = models.CharField(max_length=5000)
    time = models.CharField(max_length=100)


class Rtst(models.Model):
    userid = models.CharField(max_length=50)
    data = models.CharField(max_length=5000)
    time = models.CharField(max_length=100)


class Tcst(models.Model):
    userid = models.CharField(max_length=50)
    data = models.CharField(max_length=5000)
    time = models.CharField(max_length=100)


class Rdst(models.Model):
    userid = models.CharField(max_length=50)
    data = models.CharField(max_length=5000)
    time = models.CharField(max_length=100)


class Irms(models.Model):
    userid = models.CharField(max_length=50)
    data = models.CharField(max_length=5000)
    time = models.CharField(max_length=100)


class Bot(models.Model):
    userid = models.CharField(max_length=50)
    data = models.CharField(max_length=5000)
    time = models.CharField(max_length=100)
    img = models.CharField(max_length=300)

