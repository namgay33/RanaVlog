from django.urls import path
from Rana import views
from django.contrib import admin

from Rana import views
from .views import HomeTemplateView, AppointmentTemplateView, ManageAppointmentTemplateView


urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('', views.index, name="index"),
    path('', HomeTemplateView.as_view(), name='home'),
    path('services/', views.services, name='services'),
    path('location/', views.location, name="location"),
    path('login/', views.login, name="login"),
    path('memberlogin/', views.memberlogin, name="memberlogin"),
    path('about-us/', views.aboutus, name="aboutus"),
    path('login_first/', views.login_first, name="login_first"),
    path('data/', views.Database, name="data"),
    path('present/', views.present_data, name="presentData"),
    path('serviceproviders/', views.serviceProviders, name='serviceProviders'),
    path('book-the-service/', AppointmentTemplateView.as_view(), name='booking'),
    path('manage-booking/', ManageAppointmentTemplateView.as_view(), name='manage'),
    path('appointment/', views.appointment, name="appointment"),






]
