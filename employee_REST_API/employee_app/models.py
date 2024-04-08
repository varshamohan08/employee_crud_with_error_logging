from django.db import models

# Create your models here.
class employees(models.Model):
    regid = models.CharField(max_length=10, null=True, blank=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=50, null=True, blank=True)
    phoneNo = models.CharField(max_length=50, null=True, blank=True)
    addressDetails = models.JSONField()
    workExperience = models.JSONField()
    qualifications = models.JSONField()
    projects = models.JSONField()
    photo = models.TextField()
{
    "name": "xyz",
    "email":"xyz@gmail.com",
    "age": 25,
    "gender": "male",
    "phoneNo": "",
    "addressDetails": {
        "hno": "123",
        "street": "xyz",
        "city": "xyz",
        "state": "xyz"
    },
    "workExperience": [
    {
        "companyName": "xyz",
        "fromDate": "20-05-2019",
        "toDate": "20-09-2021",
        "address": "xyz"
    }
    ],
    "qualifications": [
    {
        "qualificationName": "ssc",
        "fromDate": "20-05-2012",
        "toDate": "20-05-2013",
        "percentage": 85
    }
    ],
    "projects": [
    {
        "titile": "xyz",
        "description": "description of the project"
    }
    ],
    "photo": "zsc"
}