from django.db import models


class Group(models.Model):
    passport = models.ImageField(null=True,upload_to='images/')
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.IntegerField(null=True)
    email = models.EmailField(null=True)
    joined_date = models.DateField(null=True)    
    
    def __str__(self):
        return f"{self.firstname} {self.lastname}"