# Generated by Django 3.0.5 on 2025-01-05 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_remove_student_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='address',
            field=models.CharField(default=False, max_length=40),
        ),
    ]