# Generated by Django 2.2.5 on 2021-03-16 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GardenApp', '0003_auto_20210316_1349'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='planner',
            name='Harvest_Time_Frame',
        ),
        migrations.AddField(
            model_name='planner',
            name='General_Care_Notes',
            field=models.TextField(blank=True, default='', max_length=500),
        ),
        migrations.AddField(
            model_name='planner',
            name='Harvest_Notes',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='planner',
            name='Sowing_Time_Frame',
            field=models.CharField(blank=True, default='', max_length=30),
        ),
    ]
