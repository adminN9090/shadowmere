# Generated by Django 3.2.8 on 2021-10-20 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Proxy",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("url", models.CharField(max_length=1024, unique=True)),
                ("location", models.CharField(default="", max_length=100)),
                ("is_active", models.BooleanField(default=False)),
                ("last_checked", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
