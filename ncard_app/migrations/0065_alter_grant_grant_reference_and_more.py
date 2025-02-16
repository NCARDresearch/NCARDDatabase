# Generated by Django 4.1.5 on 2023-01-17 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ncard_app', '0064_rename_reference_grant_grant_reference_grant_agency_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grant',
            name='grant_reference',
            field=models.CharField(blank=True, max_length=64, verbose_name='Grant Reference'),
        ),
        migrations.AlterField(
            model_name='grant',
            name='roap_reference',
            field=models.CharField(blank=True, max_length=64, verbose_name='ROAP Reference'),
        ),
        migrations.AlterField(
            model_name='grant',
            name='status',
            field=models.IntegerField(blank=True, choices=[(1, 'Application submitted'), (2, 'Grant unsuccessful'), (3, 'Current'), (4, 'Complete')], default=1, null=True, verbose_name='Status'),
        ),
    ]
