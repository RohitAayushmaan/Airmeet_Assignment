from django.db import models

# Create your models here.
class student(models.Model):
    firstName=models.CharField(max_length=30)
    lastName=models.CharField(max_length=30)
    accountNumber=models.IntegerField(max_length=20)
    email=models.EmailField(max_length=254);
    dob=models.DateField();

    def __str__(self):
        return self.firstName

