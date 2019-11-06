from django.db import models
from django import forms
#from django.forms import ModelForm
#from django.urls import reverse
#from django.contrib.auth.models import User
Lecturer1= [
    ('s','Sujjala Shetty'),
    ('p','priti bajpy' ),
    ('sa','Santosh'),
    ('k','k.kumar'),
    ]
Lecturer2= [
    ('s','Sujjala Shetty'),
    ('p','priti bajpy' ),
    ('sa','Santosh'),
    ('k','k.kumar'),
    ]

class Snipp(models.Model):
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    BITSID = models.CharField(max_length=100)
    Address = models.CharField(max_length=1000)
    Reason = models.CharField(max_length=1000)
    Email = models.EmailField()
    #RequestDate =  models.DateTimeField(default='date')
    #ReturnDate = models.DateField(default='date')
    RequestDate =models.CharField(max_length=100)
    ReturnDate = models.CharField(max_length=100)
    Lecture1 = models.CharField(max_length=100,choices=Lecturer1)
    Lecture2 = models.CharField(max_length=100,choices=Lecturer2)
    def __str__(self):
        return self.FirstName+" "+self.LastName
#User = models.ForeignKey(User, on_delete=models.CASCADE)
"""    
    class RequestForm(ModelForm):
    class Meta:
        model = Request
        fields = ['FirstName', 'LastName', 'BITSID','Address','Reason','sender']
"""





