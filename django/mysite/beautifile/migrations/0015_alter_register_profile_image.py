# Generated by Django 4.2a1 on 2023-03-02 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beautifile', '0014_remove_register_profile_pic_register_profile_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]