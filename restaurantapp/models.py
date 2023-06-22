from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
import datetime
from itertools import product
import os

def getFileName(request,filename):
  now_time=datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
  new_filename="%s%s"%(now_time,filename)
  return os.path.join('upload/',new_filename)

class Food(models.Model):
    name=models.CharField(max_length=150,null=False,blank=False)
    price=models.FloatField(null=False,blank=False)
    image=models.ImageField(upload_to=getFileName, null=True,blank=True)


   


class datastore(models.Model):
    First_name1=models.CharField(max_length=150,default="")
    Last_name1=models.CharField(max_length=30,default="")
    NO_of_persons1=models.IntegerField(default=0)
    
    phone_number1=models.TextField(max_length=40,default="")
    mail1=models.TextField(max_length=40,default="")
    Date1=models.DateField (null=True)
    Time1=models.TimeField (null=True)
class Datas(models.Model):
    First_name1=models.CharField(max_length=150,default="")
    Last_name1=models.CharField(max_length=30,default="")
    NO_of_persons1=models.IntegerField(default=0)
  
    
    phone_number1=models.TextField(max_length=40,default="")
    mail1=models.TextField(max_length=40,default="")


