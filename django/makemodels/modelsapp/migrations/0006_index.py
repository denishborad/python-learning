# Generated by Django 4.2a1 on 2023-02-18 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelsapp', '0005_contactus'),
    ]

    operations = [
        migrations.CreateModel(
            name='Index',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=200)),
                ('Last_Name', models.CharField(max_length=200)),
                ('Roll_No', models.IntegerField(help_text='Enter ^ digit rol number')),
                ('Password', models.CharField(max_length=15)),
            ],
        ),
    ]
