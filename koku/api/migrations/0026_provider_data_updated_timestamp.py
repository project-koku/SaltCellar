# Generated by Django 2.2.15 on 2020-08-23 23:26
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [("api", "0025_db_functions")]

    operations = [
        migrations.AddField(
            model_name="provider", name="data_updated_timestamp", field=models.DateTimeField(null=True)
        )
    ]
