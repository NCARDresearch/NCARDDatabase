# Generated by Django 4.1.5 on 2023-01-17 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ncard_app', '0059_alter_person_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grant',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
