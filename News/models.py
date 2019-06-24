from django.utils import timezone #import  timezone
from django.db import models #import db for models

# Create your models here.

class News(models.Model):
    author = models.CharField(max_length=30) # insert in the DB a field char max_length 30
    title = models.CharField(max_length=30) # insert in the DB a field char max_length 30
    description = models.TextField() # insert in the DB a text field
    pub_date = models.DateField(default=timezone.now()) # insert in the DB a field date

    # To see the name of the author in the description
    def __str__(self):
        return self.author



class sportNews(models.Model):
    author = models.CharField(max_length=30) # insert a field author in the DB a field char max_length 30
    title = models.CharField(max_length=30) # insert a field title in the DB a field char max_length 30
    description = models.TextField() # insert a field description  in the DB a text field

    #To see the name of the author in the description
    def __str__(self):
        return self.author


class RegistrationData(models.Model):
    username = models.CharField(max_length=100) # insert a field username in the DB a field char max_length 100
    password = models.CharField(max_length=100) # insert a field password in the DB a field char max_length 100
    email = models.CharField(max_length=100) # insert a field email in the DB a field char max_length 100
    phone = models.CharField(max_length=100) # insert a field phone in the DB a field char max_length 100

    # To see the name of the user in the panel
    def __str__(self):
        return self.username

class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='media/')
    uploaded_at = models.DateField(default=timezone.now())

    def __str__(self):
        return self.description