# Generated by Django 5.0.2 on 2024-02-10 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0005_task_model_task_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task_model',
            name='task_status',
            field=models.BooleanField(),
        ),
    ]
