# Generated by Django 4.1 on 2023-04-30 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('innstant', '0027_notification_poke'),
    ]

    operations = [
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Contact', models.IntegerField(max_length=13)),
                ('Address', models.CharField(max_length=50)),
                ('Email_us', models.CharField(max_length=50)),
                ('About', models.CharField(max_length=150)),
                ('Facebook', models.CharField(max_length=50)),
            ],
        ),
    ]
