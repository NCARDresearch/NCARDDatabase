# Generated by Django 4.1.10 on 2023-07-18 04:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ncard_app', '0072_department_person_department_other_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='department_other',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='contacts_other_dept', to='ncard_app.department', verbose_name='Department (Other)'),
        ),
        migrations.AlterField(
            model_name='person',
            name='department_primary',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='contacts_primary_dept', to='ncard_app.department', verbose_name='Department (Primary)'),
        ),
    ]
