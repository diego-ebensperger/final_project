

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import StudentForm, TeacherForm, CourseForm
from .models import Student, Teacher, Course
from .forms import UserProfileForm
from .models import UserProfile

def home(request):
    return render(request, 'school_app/home.html')

@login_required
def student_add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()
            return redirect('home')
    else:
        form = StudentForm()
    return render(request, 'school_app/student_form.html', {'form': form})

@login_required
def student_edit(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            student = form.save()
            return redirect('home')
    else:
        form = StudentForm(instance=student)
    return render(request, 'school_app/student_form.html', {'form': form})

@login_required
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    return redirect('home')

@login_required
def teacher_add(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TeacherForm()
    return render(request, 'school_app/teacher_form.html', {'form': form})

@login_required
def teacher_edit(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == "POST":
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TeacherForm(instance=teacher)
    return render(request, 'school_app/teacher_form.html', {'form': form})

@login_required
def teacher_delete(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    teacher.delete()
    return redirect('home')

@login_required
def course_add(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CourseForm()
    return render(request, 'school_app/course_form.html', {'form': form})

@login_required
def course_edit(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == "POST":
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CourseForm(instance=course)
    return render(request, 'school_app/course_form.html', {'form': form})

@login_required
def course_delete(request, pk):
    course = get_object_or_404(Course, pk=pk)
    course.delete()
    return redirect('home')

def search_results(request):
    query = request.GET.get('q')
    students = Student.objects.filter(user__username__icontains=query)
    teachers = Teacher.objects.filter(user__username__icontains=query)
    courses = Course.objects.filter(course_name__icontains=query)
    return render(request, 'school_app/search_results.html', {'students': students, 'teachers': teachers, 'courses': courses})

@login_required
def profile(request):
    user_profile = UserProfile.objects.get(user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=user_profile)
    return render(request, 'school_app/profile.html', {'form': form})