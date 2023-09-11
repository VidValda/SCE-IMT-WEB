from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_student, name='register_student'),
    path('manage-projects/', views.manage_projects, name='manage_projects'),
    path('member-listing/', views.member_listing, name='member_listing'),
]
