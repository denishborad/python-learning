# Generated by Django 4.2a1 on 2023-03-18 06:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beautifile', '0047_rename_user_email_linkgenerate_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='linkgenerate',
            name='link_id',
        ),
    ]
