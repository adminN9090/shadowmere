# Generated by Django 5.0.3 on 2024-04-01 17:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("proxylist", "0014_tasklog"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tasklog",
            name="start_time",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
