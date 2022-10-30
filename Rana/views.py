from http.client import HTTPResponse
from tokenize import Name
from urllib.request import Request
from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from . models import *
from django.db.models import Q
from django.template import Context, loader


def index(request):
    return render(request, 'index.html')


def login_first(request):
    return render(request, 'login.html')


def services(request):
    return render(request, 'services.html')
    # # return HttpResponse('hello pomp')
    # return HttpResponse("HEllo")


def location(request):
    return render(request, 'location.html')


def serviceProviders(request):
    # serviceProviders = Student.objects.all()
    return render(request, 'service_providers.html')


def login(request):
    if request.method == 'POST':
        Student_Id = request.POST.get('Student_Id')
        password = request.POST.get('password')

        try:
            user = Moderator.objects.get(Student_Id=Student_Id, password=password)
            if user is not None:
                return redirect('data')
            else:
                messages.error(request, 'username or password not correct')
                return redirect('data.html')

        except Exception as identifier:
            messages.error(request, 'username or password not correct')
            return redirect('login')

    else:
        return render(request, 'login.html')


def Database(request):
    form = Student.objects.order_by('Day').values()

    # if request.metho
    context = {'form': form}
    return render(request, 'data.html', context)


def present_data(request):
    if request.method == "POST":
        student = request.POST.getlist('student')
        print(student)
        for i in student:
            stud_id = i
            int_stud = int(stud_id)

            P_students = Student.objects.get(id=int_stud)
            attendance = Attendance(
                student=P_students
            )
            attendance.save()

        return redirect('data')
