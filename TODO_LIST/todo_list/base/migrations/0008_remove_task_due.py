# Generated by Django 4.2.2 on 2023-07-26 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_alter_task_due'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='due',
        ),
    ]
