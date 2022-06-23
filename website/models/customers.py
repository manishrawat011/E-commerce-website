from django.db import models

class Customer(models.Model):
    first_name= models.CharField(max_length=30)
    last_name= models.CharField(max_length=15)
    phone= models.CharField(max_length=13)
    email= models.EmailField()
    password= models.CharField(max_length=30)

def register(self):
    self.save()