from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class AddAttendanceForm(ModelForm):
    class Meta:
        model = Attendance
        fields = "__all__"


class AddMarksForm(ModelForm):
    class Meta:
        model = Marks
        fields = "__all__"


class AddNoticeForm(ModelForm):
    class Meta:
        model = Notice
        fields = "__all__"
