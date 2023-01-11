# Generated by Django 4.1.5 on 2023-01-11 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ncard_app', '0055_person_active_students_active_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='active',
            field=models.BooleanField(default=True, null=True, verbose_name='Active'),
        ),
        migrations.AlterField(
            model_name='students',
            name='active_student',
            field=models.BooleanField(default=True, null=True, verbose_name='Active'),
        ),
    ]
