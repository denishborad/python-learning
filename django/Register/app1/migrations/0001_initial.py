# Generated by Django 4.2a1 on 2023-02-16 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='sign_up',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=254)),
                ('pass1', models.CharField(max_length=12)),
                ('pass2', models.CharField(max_length=12)),
            ],
        ),
    ]
