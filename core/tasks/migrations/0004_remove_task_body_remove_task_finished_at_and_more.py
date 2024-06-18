# Generated by Django 4.2 on 2024-06-16 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_alter_task_finished_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='body',
        ),
        migrations.RemoveField(
            model_name='task',
            name='finished_at',
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.TextField(),
        ),
    ]