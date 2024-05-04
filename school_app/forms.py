from django import forms
from .models import Student, Teacher, Course
from django.contrib.auth.models import User
from .models import UserProfile

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('avatar',)