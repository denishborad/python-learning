# Generated by Django 4.2a1 on 2023-04-13 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0005_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='is_delete',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
