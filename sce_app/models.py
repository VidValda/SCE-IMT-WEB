from django.db import models

# Create your models here.
from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()


class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    projects = models.ManyToManyField(Project, blank=True, related_name='students')

class Membership(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
