from django.db import models

# Create your models here.
class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=180)
    email = models.EmailField(max_length=180, unique=True)
    department = models.CharField(max_length=180)
    salary = models.FloatField()
    birth_date = models.DateField()

    def __str__(self):
        return self.name