# Generated by Django 4.2a1 on 2023-03-04 05:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('beautifile', '0024_user_session'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='created',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='session',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='session',
            name='is_deleted',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='session',
            name='session_status',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='session',
            name='token',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='session',
            name='updated',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='session',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='beautifile.user'),
        ),
    ]