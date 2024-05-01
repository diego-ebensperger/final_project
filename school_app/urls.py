from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('student/add/', views.student_add, name='student_add'),
    path('student/<int:pk>/edit/', views.student_edit, name='student_edit'),
    path('student/<int:pk>/delete/', views.student_delete, name='student_delete'),
    path('teacher/add/', views.teacher_add, name='teacher_add'),
    path('teacher/<int:pk>/edit/', views.teacher_edit, name='teacher_edit'),
    path('teacher/<int:pk>/delete/', views.teacher_delete, name='teacher_delete'),
    path('course/add/', views.course_add, name='course_add'),
    path('course/<int:pk>/edit/', views.course_edit, name='course_edit'),
    path('course/<int:pk>/delete/', views.course_delete, name='course_delete'),
    path('search/', views.search_results, name='search_results'),
    
    ]
