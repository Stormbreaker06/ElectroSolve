# Generated by Django 5.1.6 on 2025-02-09 16:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0004_problem_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='problem',
            name='options',
        ),
    ]
