from django.shortcuts import render, redirect
from .models import Student, Project, Membership
from .forms import RegistrationForm, ProjectForm
# Create your views here.

def register_student(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            student = form.save()
            # Handle membership registration here
            return redirect('member_listing')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def manage_projects(request):
    # Handle project management logic here
    return render(request, 'manage_projects.html')

def member_listing(request):
    projects = Project.objects.all()
    if request.GET.get('project'):
        project_id = request.GET.get('project')
        students = Student.objects.filter(membership__project_id=project_id)
    else:
        students = Student.objects.all()

    return render(request, 'member_listing.html', {'students': students, 'projects': projects})
