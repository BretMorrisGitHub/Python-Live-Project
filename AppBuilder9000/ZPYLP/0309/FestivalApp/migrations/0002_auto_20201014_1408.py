# Generated by Django 2.2.5 on 2020-10-14 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FestivalApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='festivalreview',
            name='comment',
            field=models.TextField(blank=True, default='', max_length=1000),
        ),
    ]