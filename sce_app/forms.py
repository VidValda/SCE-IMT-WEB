from django import forms
from .models import Student, Project
from .widgets import ProjectCheckboxSelectMultiple

class RegistrationForm(forms.ModelForm):
    projects = forms.ModelMultipleChoiceField(
        queryset=Project.objects.all(),
        widget=ProjectCheckboxSelectMultiple,  # Use the custom widget
    )

    class Meta:
        model = Student
        fields = ['first_name','last_name','cellphone', 'email', 'projects']  # Define the order of fields

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description']  # Add other project-related fields here

class FilterForm(forms.Form):
    project = forms.ModelChoiceField(
        queryset=Project.objects.all(),
        required=False,  # Allow selecting "All Projects"
        empty_label="All Projects"  # Display "All Projects" as the default option
    )
