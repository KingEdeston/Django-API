from django import forms
from .models import StudentData


class CreateNewList(forms.ModelForm):
    firstname = forms.CharField(label="First Name", max_length=200)
    lastname = forms.CharField(label="Last Name", max_length=200)
    wid = forms.CharField(label="WID", max_length=20)
    courses = forms.CharField(label="Courses", max_length=200)
    class Meta:
        model = StudentData
        fields = '__all__'

class SearchNewList(forms.ModelForm):
    class Meta:
        model = StudentData
        fields = '__all__'