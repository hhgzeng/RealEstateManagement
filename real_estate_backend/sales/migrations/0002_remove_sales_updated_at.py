# Generated by Django 4.2.17 on 2025-01-10 06:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sales',
            name='updated_at',
        ),
    ]