from unicodedata import name
from django.db import models
from sqlalchemy import true

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=20,null=True)
    age=models.IntegerField(null=True)
    course=models.CharField(max_length=20,null=True)
    depart=models.CharField(max_length=20,null=True)


    def __str__ (self):
        return f'name : {self.name},course :{self.course}'

class Lec(models.Model):
    name=models.CharField(max_length=20,null=True,blank=True)
    id=models.IntegerField(primary_key=True,blank=True)
    course=models.CharField(max_length=200,null=True,blank=True)
    school=models.CharField(max_length=200,null=True,blank=True)
        
def __str__(self):
    return f'name{self.name}'
        