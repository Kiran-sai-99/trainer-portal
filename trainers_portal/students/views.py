from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import StudentForm
from .models import Student

# Create your views here.
@login_required(login_url='signin')
def create_student_view(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)

        if form.is_valid():
            student = form.save(commit=False)
            student.trainer = request.user
            student.save()
            return redirect('display')
    else:
        form = StudentForm()

    context = {
        'form' : form,
        'title' : 'Create Student',
        'operation' : '+ Add Student'
    }

    return render(request, 'form.html', context)


@login_required(login_url='signin')
def display_students_view(request):
    students = Student.objects.filter(trainer=request.user)

    context = {
        'students' : students
    }

    return render(request, 'students-display.html', context)


@login_required(login_url='signin')
def delete_student_view(request, id):
    student = get_object_or_404(Student, id=id)
    
    if request.method == 'POST':
        student.delete()
        return redirect('display')
    
    context = {
        'student' : student,
        'operation' : '- Delete Student',
    }

    return render(request, 'delete-student.html', context)


@login_required(login_url='signin')
def update_student_view(request, id):
    student = get_object_or_404(Student, id=id)
    
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)

        if form.is_valid():
            form.save()
            return redirect('display')
        
    else:
        form = StudentForm(instance=student)

    context = {
        'form' : form,
        'title' : 'Update Student',
        'operation' : '* Update'
    }

    return render(request, 'student-update.html', context)
