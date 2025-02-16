# Generated by Django 4.1.3 on 2024-12-03 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedulingappapi', '0006_alter_task_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='category',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='duration',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='end_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='start_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
