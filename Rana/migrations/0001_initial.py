# Generated by Django 4.0.5 on 2022-10-18 03:51

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.TextField(max_length=255)),
                ('Student_Id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.TextField(max_length=255)),
                ('Student_Id', models.IntegerField()),
                ('Day', models.TextField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            managers=[
                ('empAuth_objects', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_attendance', models.IntegerField(default=0)),
                ('usn', models.ForeignKey(db_column='usn', on_delete=django.db.models.deletion.CASCADE, to='Rana.student')),
            ],
        ),
    ]
