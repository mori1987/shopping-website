
from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message= models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name}'

