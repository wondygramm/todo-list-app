# Generated by Django 4.2.2 on 2023-07-18 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_remove_task_due_task_deadline'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='deadline',
            new_name='due',
        ),
    ]
