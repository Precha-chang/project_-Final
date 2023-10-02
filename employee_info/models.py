from django.db import models

# Create your models here.
class Department(models.Model):

    department = models.CharField(max_length=255)

    def str(self):
        return self.department

class Information(models.Model):

    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    age = models.IntegerField()
    elevel = models.CharField(max_length=255)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)


    def str(self):
        return self.title