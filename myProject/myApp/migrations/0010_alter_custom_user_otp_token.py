# Generated by Django 5.0.2 on 2024-02-13 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0009_custom_user_otp_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custom_user',
            name='otp_token',
            field=models.CharField(max_length=10, null=True),
        ),
    ]