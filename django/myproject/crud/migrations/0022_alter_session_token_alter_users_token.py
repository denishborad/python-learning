# Generated by Django 4.2a1 on 2023-04-24 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0021_users_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='token',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='token',
            field=models.CharField(max_length=500, null=True),
        ),
    ]