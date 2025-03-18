from django.shortcuts import render,HttpResponse,redirect
from .forms import studentForm,TeacherForm
from .models import student
from django.contrib.admin.views.decorators import staff_member_required
from django.conf import settings
from dashboard.views import dashboard_view
LOGIN_URL = settings.LOGIN_URL

# Create your views here.

# @staff_member_required(login_url=LOGIN_URL)
def studentList(request):
    if request.user.is_authenticated:
        return dashboard_view(request)
    students = student.objects.all()
    context ={
        'students':students,
    }
    return render(request,'student/student_list.html',context)

def studentCreate(request):
    form = studentForm()
    if request.method == "POST":
        form = studentForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('student_list')
        
    context={
        'form':form,
    }

    
    return render(request,'student/student_create.html',context)
def TeacherCreate(request):
    form = TeacherForm()
    if request.method == "POST":
        form = TeacherForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('student_list')
        
    context={
        'form':form,
    }

    
    return render(request,'student/teacher_create.html',context)

def studentDelete(request,pk):
    
    Student = student.objects.get(student_id=pk)
    if request.method == "POST":
        Student.delete()
        return redirect('student_list')
    
    context={
        'Student':Student
    }
        
    return render(request,'student/delete_student.html',{'obj':Student})
