# Generated by Django 4.2a1 on 2023-02-21 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beautifile', '0003_products'),
    ]

    operations = [
        migrations.CreateModel(
            name='addprouct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ptitle', models.CharField(max_length=50)),
                ('pdesc', models.CharField(max_length=200)),
                ('pimages', models.ImageField(upload_to='')),
                ('pprice', models.IntegerField()),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
