# Generated by Django 4.2a1 on 2023-03-17 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beautifile', '0043_remove_userdetails_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='LinkGenerate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link_id', models.CharField(max_length=200)),
                ('user_id', models.CharField(max_length=500)),
                ('user_email', models.EmailField(max_length=254)),
                ('token', models.CharField(max_length=250)),
                ('expiry', models.DateTimeField()),
                ('status', models.BooleanField()),
            ],
        ),
    ]
