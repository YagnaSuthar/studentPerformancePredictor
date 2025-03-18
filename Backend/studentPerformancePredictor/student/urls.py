from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.studentList ,name="student_list"),
    path('create-student/',views.studentCreate,name='create_student'),
    path('create-Teacher/',views.TeacherCreate,name='create_teacher'),
    path('student/<int:pk>/',views.student,name="student_list"),
    path('student_delete/<int:pk>/',views.studentDelete,name="student_delete"),
]
