# Generated by Django 4.2.2 on 2023-08-25 13:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_centraluser'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CentralUser',
        ),
    ]