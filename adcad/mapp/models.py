from django.db import models


class Group(models.Model):
    passport = models.ImageField(null=True,upload_to='images/')
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.IntegerField(null=True)
    email = models.EmailField(null=True)
    joined_date = models.DateField(null=True)  
    about = models.TextField(null=True)  
    
    ca1 = models.IntegerField(default=0)
    ca2 = models.IntegerField(default=0)
    ca3 = models.IntegerField(default=0)
    
    @property
    def total(self):
        return self.ca1 + self.ca2 + self.ca3
    
    def __str__(self):
        return f"{self.firstname} {self.lastname}"
    
    
# from django.db import models

# class InputTable(models.Model):
#     teacher = models.ForeignKey(Group, on_delete=models.CASCADE, null=True)
#     input1 = models.FloatField(default=0)
#     input2 = models.FloatField(default=0)
#     input3 = models.FloatField(default=0)

#     def total(self):
#         return self.input1 + self.input2 + self.input3
