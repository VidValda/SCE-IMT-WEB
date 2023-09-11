from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Project, Membership
from .forms import RegistrationForm, ProjectForm, FilterForm
# Create your views here.
def home(request):
    return render(request, 'home.html')


def register_student(request):
    projects = Project.objects.all()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            student = form.save()
            # Handle membership registration here
            return redirect('member_listing')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form, 'projects': projects})

def manage_projects(request):
    if request.method == 'POST':
        # Handle the form submission for project creation or updates
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            # You can add success messages or redirection logic here
            return redirect('manage_projects')
    else:
        # Display the form for creating or updating projects
        form = ProjectForm()

    # Query all existing projects to display in the template
    projects = Project.objects.all()

    return render(request, 'manage_projects.html', {'form': form, 'projects': projects})

def delete_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if request.method == 'POST':
        project.delete()
        # You can add success messages or redirection logic here
        return redirect('manage_projects')
    return render(request, 'confirm_delete_project.html', {'project': project})

def member_listing(request):

    # Initialize the form
    form = FilterForm(request.GET)

    # Filter students based on the selected project
    students = Student.objects.all()

    # Check if a project is selected in the form
    if form.is_valid() and form.cleaned_data['project']:
        project = form.cleaned_data['project']
        students = students.filter(projects=project)

    # Pass the projects and filtered students to the template
    return render(request, 'member_listing.html', {'form': form, 'students': students})