# Generated by Django 4.2a1 on 2023-03-04 06:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beautifile', '0025_session_created_session_email_session_is_deleted_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Session',
        ),
    ]
