# Generated by Django 4.1 on 2023-04-22 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('innstant', '0021_extendstay_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
