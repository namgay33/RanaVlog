from django.contrib import admin
from .models import Student, Attendance, Moderator, Booking, ItsLogBook

admin.site.register(Student)

admin.site.register(Attendance)
admin.site.register(Moderator)
admin.site.register(Booking)
admin.site.register(ItsLogBook)
