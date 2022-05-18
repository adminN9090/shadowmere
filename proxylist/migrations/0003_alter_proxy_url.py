# Generated by Django 3.2.11 on 2022-02-09 14:26

from django.db import migrations, models
import proxylist.models


class Migration(migrations.Migration):

    dependencies = [
        ("proxylist", "0002_proxy_last_active"),
    ]

    operations = [
        migrations.AlterField(
            model_name="proxy",
            name="url",
            field=models.CharField(
                max_length=1024,
                unique=True,
                validators=[proxylist.models.validate_not_existing],
            ),
        ),
    ]
