# Generated by Django 4.1 on 2022-10-30 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rana', '0012_student_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='contact',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
