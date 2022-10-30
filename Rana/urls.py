from django.urls import path
from Rana import views
from django.contrib import admin

from Rana import views


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('services/', views.services, name='services'),
    path('location/', views.location, name="location"),
    path('login/', views.login, name="login"),
    path('login_first/', views.login_first, name="login_first"),
    path('data/', views.Database, name="data"),
    path('present/', views.present_data, name="presentData"),
    path('serviceproviders/', views.serviceProviders, name='serviceProviders')



    # path('home', views.home, name='home')
]
