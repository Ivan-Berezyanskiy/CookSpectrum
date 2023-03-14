# Generated by Django 4.1 on 2023-03-11 13:54

from django.db import migrations
from django.db.migrations import RunPython


def func(apps, schema_editor):
    from django.core.management import call_command
    call_command('loaddata', 'data.json')


def reverse_func(apps, schema_editor):
    pass


class Migration(migrations.Migration):
    dependencies = [
        ("kitchen", "0001_initial"),
    ]

    operations = [
        RunPython(func, reverse_func)
    ]