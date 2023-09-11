from django import forms
from .models import Student, Project

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email','projects']  # Add other student-related fields here

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description']  # Add other project-related fields here
