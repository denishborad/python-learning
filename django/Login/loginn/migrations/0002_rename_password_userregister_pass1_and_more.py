# Generated by Django 4.2a1 on 2023-02-15 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loginn', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userregister',
            old_name='password',
            new_name='pass1',
        ),
        migrations.RenameField(
            model_name='userregister',
            old_name='repassword',
            new_name='pass2',
        ),
    ]