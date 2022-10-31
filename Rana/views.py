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


from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.core.mail import EmailMessage, message
from django.conf import settings
from django.contrib import messages
from .models import Booking
from django.views.generic import ListView
import datetime
from django.template import Context
from django.template.loader import render_to_string, get_template


class HomeTemplateView(TemplateView):
    template_name = "index.html"

    def post(self, request):
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        email = EmailMessage(
            subject=f"{name}",
            body=message,
            from_email=settings.EMAIL_HOST_USER,
            to=[settings.EMAIL_HOST_USER],
            reply_to=[email]
        )
        email.send()
        messages.add_message(request, messages.SUCCESS,
                             f"Thank you for booking the service.")
        return HttpResponseRedirect(request.path)


class AppointmentTemplateView(TemplateView):
    template_name = "services.html"

    def post(self, request):
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        email = request.POST.get("email")
        mobile = request.POST.get("mobile")
        message = request.POST.get("request")

        appointment = Booking.objects.create(
            first_name=fname,
            last_name=lname,
            email=email,
            phone=mobile,
            request=message,
        )

        appointment.save()

        messages.add_message(request, messages.SUCCESS,
                             f"Thanks {fname} for booking the service.")
        return HttpResponseRedirect(request.path)


class ManageAppointmentTemplateView(ListView):
    template_name = "manage-appointments.html"
    model = Booking
    context_object_name = "appointments"
    login_required = True
    paginate_by = 3

    def post(self, request):
        date = request.POST.get("date")
        appointment_id = request.POST.get("appointment-id")
        appointment = Booking.objects.get(id=appointment_id)
        appointment.accepted = True
        appointment.accepted_date = datetime.datetime.now()
        appointment.save()

        data = {
            "fname": appointment.first_name,
            "date": date,
        }

        message = get_template('email.html').render(data)
        email = EmailMessage(
            "About your Booking",
            message,
            settings.EMAIL_HOST_USER,
            [appointment.email],
        )
        email.content_subtype = "html"
        email.send()

        messages.add_message(request, messages.SUCCESS,
                             f"You accepted the service request of {appointment.first_name}")
        return HttpResponseRedirect(request.path)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        appointments = Booking.objects.all()
        context.update({
            "title": "Manage Bookings"
        })
        return context


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


def aboutus(request):
    return render(request, 'about.html')


def serviceProviders(request):
    form = Student.objects.order_by('Day').values()

    # if request.metho
    context = {'form': form}
    return render(request, 'service_providers.html', context)


def login(request):
    if request.method == 'POST':
        Student_Id = request.POST.get('Student_Id')
        password = request.POST.get('password')

        try:
            user = Moderator.objects.get(
                Student_Id=Student_Id, password=password)
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


def memberlogin(request):
    if request.method == 'POST':
        Student_Id = request.POST.get('Student_Id')
        password = request.POST.get('password')

        try:
            user = Student.objects.get(
                Student_Id=Student_Id, password=password)
            if user is not None:
                return redirect('appointment')
            else:
                messages.error(request, 'username or password not correct')
                return redirect('loginMembers.html')

        except Exception as identifier:
            messages.error(request, 'username or password not correct')
            return redirect('memberlogin')

    else:
        return render(request, 'loginMembers.html')


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


def appointment(request):
    if request.method == "POST":
        name = request.POST.get("service_provider")
        service = request.POST.get("service")
        Customer_id = request.POST.get("Customer_id")
        Rate = request.POST.get("Rate")
        Remarks = request.POST.get("Remarks")
        Date = request.POST.get("Date")

        # print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
        # print(name)
        appointment = ItsLogBook(
            Name=name,
            service=service,
            customer_Id=Customer_id,
            Remarks=Remarks,
            Rate=Rate,
            Date=Date
        )
        appointment.save()

    messages.add_message(request, messages.SUCCESS,
                         "Thanks for making an appointment, we will email you ASAP!")
    return render(request, 'appointment.html', )
