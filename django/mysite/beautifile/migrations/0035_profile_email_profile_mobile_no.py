# Generated by Django 4.2a1 on 2023-03-07 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beautifile', '0034_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='mobile_no',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
