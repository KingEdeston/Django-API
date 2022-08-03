from unicodedata import name
from django.db import models

#Create your models here.
class Roster(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Item(models.Model):
    wid = models.CharField(max_length = 20, default="000000")
    lastName = models.CharField(max_length = 25, default="Smith")
    roster = models.ForeignKey(Roster, on_delete=models.CASCADE, null=True)
    text = models.CharField(max_length=300)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.text

class CertForm(models.Model):
    firstname = models.CharField(max_length = 100, default="John")
    lastname = models.CharField(max_length = 100, default="Doe")
    wid = models.CharField(max_length = 10, default="0000000000")
    courses = models.CharField(max_length = 100, default="None")

class StudentData(models.Model):
    firstname = models.CharField(max_length = 100, default="John")
    lastname = models.CharField(max_length = 100, default="Doe")
    wid = models.CharField(max_length = 10, default="0000000000")
    courses = models.CharField(max_length = 100, default="None")
        
    def __str__(self):
        return self.headline