from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from .forms import *


def home(request):
    notice = Notice.objects.all()
    attendance = Attendance.objects.all()
    marks = Marks.objects.all()

    context = {
        'notice': notice,
        'marks': marks,
        'attendance': attendance,
    }
    return render(request, 'school/home.html', context)


def addAttendance(request):
    if request.user.is_authenticated:
        form = AddAttendanceForm()
        if request.method == 'POST':
            form = AddAttendanceForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
        context = {'form': form}
        return render(request, 'school/addAttendance.html', context)
    else:
        return redirect('home')


def addMarks(request):
    if request.user.is_authenticated:
        form = AddMarksForm()
        if request.method == 'POST':
            form = AddMarksForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
        context = {'form': form}
        return render(request, 'school/addMarks.html', context)
    else:
        return redirect('home')


def addNotice(request):
    if request.user.is_authenticated:
        form = AddNoticeForm()
        if request.method == 'POST':
            form = AddNoticeForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
        context = {'form': form}
        return render(request, 'school/addNotice.html', context)
    else:
        return redirect('home')


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                return redirect('login')
        context = {
            'form': form,
        }
        return render(request, 'school/register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
        context = {}
        return render(request, 'school/login.html', context)


def logoutPage(request):
    logout(request)
    return redirect('/')
