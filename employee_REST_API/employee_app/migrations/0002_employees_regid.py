# Generated by Django 5.0.4 on 2024-04-04 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employees',
            name='regid',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]