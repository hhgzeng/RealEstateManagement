# Generated by Django 4.2.17 on 2025-01-10 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0002_remove_sales_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='sales',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='更新时间'),
        ),
    ]
