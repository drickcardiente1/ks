# Generated by Django 4.1 on 2023-04-22 02:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('innstant', '0020_alter_agreement_test_date_alter_complaint_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='extendstay',
            name='date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
