from django.forms import ModelForm
from .models import student,Teacher

class studentForm(ModelForm):
    class Meta:
        model = student
        fields = '__all__'

class TeacherForm(ModelForm):
    class Meta:
        model=Teacher
        fields = '__all__'
        # exclude = ['host']