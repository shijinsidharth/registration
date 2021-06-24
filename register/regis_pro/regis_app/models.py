from django.db import models
from django.db.models.fields.related import ForeignKey


    
class Login(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    def __str__(self):
        return self.username
 
class Registration(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)  
    email=models.CharField(max_length=254)
    login=ForeignKey(Login,on_delete=models.CASCADE)
    propic=models.FileField(upload_to='gallery/')

class Card(models.Model):
    title=models.CharField(max_length=30)
    description=models.TextField()
    photo=models.FileField(upload_to='gallery/')
