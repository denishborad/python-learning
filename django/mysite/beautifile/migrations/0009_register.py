# Generated by Django 4.2a1 on 2023-02-22 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beautifile', '0008_delete_register'),
    ]

    operations = [
        migrations.CreateModel(
            name='REGISTER',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=12)),
                ('repassword', models.CharField(max_length=12)),
            ],
        ),
    ]