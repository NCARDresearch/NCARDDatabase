# Generated by Django 4.1.5 on 2023-01-19 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ncard_app', '0068_alter_person_active_alter_students_active_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grant',
            name='bu_no',
            field=models.CharField(blank=True, max_length=64, verbose_name='Business Unit Number (BU)'),
        ),
        migrations.AlterField(
            model_name='grant',
            name='pg_no',
            field=models.CharField(blank=True, max_length=64, verbose_name='Project Grant Number (PG)'),
        ),
    ]
