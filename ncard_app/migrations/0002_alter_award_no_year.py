# Generated by Django 4.1 on 2022-09-04 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ncard_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='award',
            name='no_year',
            field=models.DecimalField(blank=True, decimal_places=1, default=1.0, max_digits=10, null=True, verbose_name='Noyear'),
        ),
    ]
