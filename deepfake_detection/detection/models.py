from django.db import models

# Create your models here.

# cl email = ass Contact(models.Model):
#    models.CharField(max_length=150)
     
class contact(models.Model):  # Make sure 'Contact' is defined
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
