# Generated by Django 4.2a1 on 2023-04-14 06:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('crud', '0008_alter_signup_firstname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='userprof',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
