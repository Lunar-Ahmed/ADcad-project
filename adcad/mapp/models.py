from django.db import models


class Group(models.Model):
    passport = models.ImageField(null=True,upload_to='images/')
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.IntegerField(null=True)
    email = models.EmailField(null=True)
    joined_date = models.DateField(null=True)  
    about = models.TextField(null=True)  
    
    def __str__(self):
        return f"{self.firstname} {self.lastname}"
    
    
from django.db import models

class InputTable(models.Model):
    teacher = models.ForeignKey(Group, on_delete=models.CASCADE)
    input1 = models.FloatField(default=0)
    input2 = models.FloatField(default=0)
    input3 = models.FloatField(default=0)

    def total(self):
        return self.input1 + self.input2 + self.input3
