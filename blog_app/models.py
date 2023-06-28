from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
Gender = (
    ("Male","Male"),
    ("Female","Female"),
    ("Other","Other")
)

class Branch(models.Model):
    branch = models.CharField(max_length=255)
    def __str__(self):
        return self.branch 

class blog(models.Model):
    heading=models.CharField(max_length=200)
    description=models.CharField(max_length=10000)
    image = CloudinaryField('image')
    submit=models.CharField(max_length=250)
    gender = models.CharField(choices=Gender,max_length=255,default="Male")
    branch = models.ForeignKey(Branch,on_delete=models.CASCADE)

    def __str__(self):
        return self.heading
    


class contects(models.Model):
    name=models.CharField(max_length=255)
    mobile=models.IntegerField()



