from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    enrollment_id = models.CharField(max_length=20)
    date_of_birth = models.DateField()

    def __str__(self):
        return self.user.username

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    employee_id = models.CharField(max_length=20)
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_code = models.CharField(max_length=10)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student)

    def __str__(self):
        return self.course_name
    

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='avatars/default.jpg', upload_to='avatars/')

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.avatar.path)

        if img.height > 300 or img.width > 300:
            img.thumbnail((300, 300))
            img.save(self.avatar.path)