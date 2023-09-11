from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_student, name='register_student'),
    path('manage-projects/', views.manage_projects, name='manage_projects'),
    path('delete-project/<int:project_id>/', views.delete_project, name='delete_project'),  
    path('member-listing/', views.member_listing, name='member_listing'),
]
