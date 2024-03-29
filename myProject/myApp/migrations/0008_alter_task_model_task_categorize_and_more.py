# Generated by Django 5.0.2 on 2024-02-12 05:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0007_alter_task_model_task_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task_model',
            name='task_categorize',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myApp.task_catagorze'),
        ),
        migrations.AlterField(
            model_name='task_model',
            name='task_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='task_model',
            name='task_priroty',
            field=models.CharField(blank=True, choices=[('Heigh', 'Heigh'), ('Medium', 'Medium'), ('Low', 'Low')], max_length=500, null=True),
        ),
    ]
