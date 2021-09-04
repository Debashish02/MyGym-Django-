from django.db import models

# Create your models here.

class Contact(models.Model):
    email = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    mobile =  models.IntegerField()
    text = models.TextField(max_length=500)
    def __str__(self):
        return self.name
