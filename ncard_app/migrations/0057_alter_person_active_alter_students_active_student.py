# Generated by Django 4.1.5 on 2023-01-12 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ncard_app', '0056_alter_person_active_alter_students_active_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Active'),
        ),
        migrations.AlterField(
            model_name='students',
            name='active_student',
            field=models.BooleanField(default=True, verbose_name='Active'),
        ),
    ]
