# Generated by Django 4.1 on 2022-10-30 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rana', '0008_appointment'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItsLogBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('service', models.TextField(blank=True)),
                ('Date', models.DateField()),
                ('customer_Id', models.IntegerField()),
                ('Rate', models.CharField(max_length=6)),
                ('Remarks', models.CharField(max_length=120)),
            ],
        ),
    ]
