# Generated by Django 5.1.3 on 2024-11-26 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedulingappapi', '0004_schedule_dates'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='goals',
            field=models.CharField(default='', max_length=10000),
            preserve_default=False,
        ),
    ]
