# Generated by Django 4.2a1 on 2023-02-10 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Subject', models.CharField(max_length=200)),
                ('Yourname', models.CharField(max_length=100)),
                ('Yourmail', models.EmailField(max_length=254)),
                ('Massege', models.TextField()),
            ],
        ),
    ]