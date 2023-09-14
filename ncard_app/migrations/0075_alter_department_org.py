# Generated by Django 4.1.10 on 2023-08-03 02:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ncard_app', '0074_rename_person_surname_2b0d3e_idx_person_surname_b68bb2_idx_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='org',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='org_depts', to='ncard_app.organisation', verbose_name='Organisation'),
        ),
    ]
