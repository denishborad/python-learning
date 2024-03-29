# Generated by Django 4.2a1 on 2023-03-04 07:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('beautifile', '0026_delete_session'),
    ]

    operations = [
        migrations.CreateModel(
            name='Session',
            fields=[
                ('session_id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('token', models.CharField(max_length=50, null=True)),
                ('session_status', models.BooleanField(null=True)),
                ('created', models.DateTimeField(null=True)),
                ('updated', models.DateTimeField(null=True)),
                ('is_deleted', models.BooleanField(null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='beautifile.user')),
            ],
        ),
    ]
