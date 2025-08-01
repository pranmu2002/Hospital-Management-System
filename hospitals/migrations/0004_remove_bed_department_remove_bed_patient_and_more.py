# Generated by Django 5.2.1 on 2025-08-01 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitals', '0003_department_bed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bed',
            name='department',
        ),
        migrations.RemoveField(
            model_name='bed',
            name='patient',
        ),
        migrations.AddField(
            model_name='patient',
            name='bed_number',
            field=models.CharField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='department',
            field=models.CharField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='Department',
        ),
        migrations.DeleteModel(
            name='Bed',
        ),
    ]
