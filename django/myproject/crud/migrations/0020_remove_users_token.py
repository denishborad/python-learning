# Generated by Django 4.2a1 on 2023-04-24 05:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0019_users_token'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='token',
        ),
    ]
