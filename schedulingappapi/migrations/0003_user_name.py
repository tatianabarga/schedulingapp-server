# Generated by Django 4.1.3 on 2024-11-21 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedulingappapi', '0002_task_category_task_locked_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(default='test', max_length=50),
            preserve_default=False,
        ),
    ]
