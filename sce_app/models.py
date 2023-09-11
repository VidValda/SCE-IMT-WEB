from django.db import models

# Create your models here.
from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    def __str__(self):
        return self.title  # Return the title as the string representation


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    cellphone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(unique=True)
    projects = models.ManyToManyField(Project, blank=True, related_name='students')

class Membership(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
