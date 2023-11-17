from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name

class Signup(models.Model):
    first_name = models.CharField(max_length=122)
    last_name = models.CharField(max_length=122)
    username = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    password1 = models.CharField(max_length=12)
    password2 = models.CharField(max_length=12)

    def __str__(self):
        return self.name
    
class login(models.Model):
    username = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    password = models.CharField(max_length=12)

    def __str__(self):
        return self.name
    
