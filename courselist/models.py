from django.db import models

# Create your models here.


class Course(models.Model):
    courseTitle = models.CharField(max_length=100)
    courseCode = models.CharField(max_length=6)
    creditHours = models.CharField(max_length=2)