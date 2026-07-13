from django.db import models


class Student(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    age = models.PositiveIntegerField()
    branch = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=10)
    city = models.CharField(max_length=50)
    cgpa = models.DecimalField(max_digits=3, decimal_places=2)
    photo = models.ImageField(upload_to='students/')

    def __str__(self):
        return self.name