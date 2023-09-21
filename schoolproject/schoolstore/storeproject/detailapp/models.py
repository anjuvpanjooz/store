from django.db import models
from django.urls import reverse


class Course(models.Model):
    dep_name=models.CharField(max_length=250 ,unique=True)
    sub_course=models.CharField(max_length=250,blank=True)
    desc=models.TextField(blank=True)
    duration=models.IntegerField(blank=True)
    def get_url(self):
        return reverse('detailapp:detail',args=[self.id])

    def __str__(self):
        return self.dep_name
class ContactQuery(models.Model):
    Name=models.CharField(max_length=250,unique=True)
    DOB=models.CharField (max_length=250,blank=True)
    age = models.TextField(blank=True)
    gender=models.TextField()
    phone_number=models.TextField()
    email_id=models.EmailField()
    address=models.TextField()
    department_choices=(('computer_science','COMPUTER_SCIENCE'),
    ('commerce', 'COMMERCE'),
    ('science','SCIENCE'),
    ('humanities','HUMANITIES'),
    ('arts','ARTS'),
    )
    dep = models.CharField(max_length=30, choices=department_choices)
    courses_choices = (('bca', 'BCA'),
                          ('bcom', 'BCOM'),
                          ('bsc', 'BSC'),
                          ('bba', 'BBA'),
                          ('bfa', 'BFA'),
                          )
    courses= models.CharField(max_length=25, choices=courses_choices)
    purpose_choices = (('enquiry', 'ENQUIRY'),
                          ('commerce', 'PLACEORDER'),
                          ('return', 'RETURN'),
                          )
    purpose = models.CharField(max_length=20, choices=purpose_choices)

    materials_provide = models.BooleanField(default=True)

    def __str(self):
        return self.Name












