# Generated by Django 4.2a1 on 2023-03-07 07:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beautifile', '0042_rename_username_userdetails_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdetails',
            name='User',
        ),
    ]
