# Generated by Django 5.1.6 on 2025-02-09 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0005_remove_problem_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='options',
            field=models.TextField(default='No options provided'),
        ),
    ]
