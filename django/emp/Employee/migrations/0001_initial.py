# Generated by Django 4.2a1 on 2023-03-28 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('emp_id', models.AutoField(primary_key=True, serialize=False)),
                ('emp_name', models.CharField(max_length=100)),
                ('emp_email', models.EmailField(max_length=254)),
                ('emp_address', models.TextField()),
                ('emp_phone', models.CharField(max_length=12)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_delete', models.BooleanField(default=False)),
            ],
        ),
    ]
