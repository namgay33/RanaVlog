from tkinter import CASCADE
from django.db import models
from django.forms import IntegerField
from traitlets import default
from django import forms


class Student(models.Model):
    # usn = models.CharField(max_length=10,primary_key=True)
    Name = models.TextField(max_length=255)
    Student_Id = models.IntegerField()
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
# Create your models here.
