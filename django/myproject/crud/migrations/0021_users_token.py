# Generated by Django 4.2a1 on 2023-04-24 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0020_remove_users_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='token',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
