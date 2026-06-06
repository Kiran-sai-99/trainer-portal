from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
    STUDENT_COURSES = {
        'Java Full Stack' : 'Java Full Stack',
        'Python Full Stack' : 'Python Full Stack',
        'MERN Stack' : 'MERN Stack',
        'AI/ML' : 'AI/ML',
        'Data Science' : 'Data Science',
        'Devops' : 'Devops'
    }

    name = models.CharField(max_length=50)
    rollno = models.IntegerField()
    email = models.EmailField(null=True, blank=True)
    contact = models.CharField(max_length=13)
    course = models.CharField(max_length=200, choices=STUDENT_COURSES)
    address = models.TextField()

    trainer = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.name