# Generated by Django 4.2a1 on 2023-03-06 07:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beautifile', '0030_login_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='register',
            old_name='uname',
            new_name='user',
        ),
    ]
