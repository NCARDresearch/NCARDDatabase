# Generated by Django 4.1.5 on 2023-01-10 07:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ncard_app', '0051_alter_person_active_alter_students_active_student'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='active',
        ),
        migrations.RemoveField(
            model_name='students',
            name='active_student',
        ),
    ]
