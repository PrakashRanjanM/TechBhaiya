from django.db import models

# Create your models here.

class Contact(models.Model):
    Sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=13)
    content = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True , blank =True)

    def __str__(self):
        return 'Message From '+ self.name

class Flames(models.Model):
    name1 = models.CharField(max_length=25)
    name2 = models.CharField(max_length=25)
    timeStamp = models.DateTimeField(auto_now_add=True , blank = True)

    def __str__(self):
        return "Flames Test From :" + self.name1