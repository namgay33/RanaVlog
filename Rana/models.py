from tkinter import CASCADE
from django.db import models
from django.forms import IntegerField
from traitlets import default
from django import forms


class Student(models.Model):
    # usn = models.CharField(max_length=10,primary_key=True)
    Name = models.TextField(max_length=255)
    Student_Id = models.IntegerField()
    password = models.CharField(max_length=255)
    contact = models.IntegerField()
    Day = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Name
    objects = models.Manager()


class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    Name = models.TextField(max_length=255)

    def __str__(self):
        return str(self.student)


class Moderator(models.Model):
    Name = models.CharField(max_length=255)
    Student_Id = models.IntegerField()
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.Name


class Booking(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    request = models.TextField(blank=True)
    sent_date = models.DateField(auto_now_add=True)
    accepted = models.BooleanField(default=False)
    accepted_date = models.DateField(auto_now_add=False, null=True, blank=True)

    def __str__(self):
        return self.first_name

    class Meta:
        ordering = ['-sent_date']


class ItsLogBook(models.Model):
    Name = models.IntegerField()
    service = models.TextField(blank=True)
    Date = models.DateField()
    customer_Id = models.IntegerField()
    Rate = models.CharField(max_length=6)
    Remarks = models.CharField(max_length=120)

    def __str__(self):
        return str(self.Name)
