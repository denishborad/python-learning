# Generated by Django 4.2a1 on 2023-03-18 06:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beautifile', '0046_alter_linkgenerate_link_id_alter_linkgenerate_token'),
    ]

    operations = [
        migrations.RenameField(
            model_name='linkgenerate',
            old_name='user_email',
            new_name='email',
        ),
    ]
