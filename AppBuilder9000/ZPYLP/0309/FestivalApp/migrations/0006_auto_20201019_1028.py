# Generated by Django 2.2.5 on 2020-10-19 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FestivalApp', '0005_auto_20201014_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='festivalreview',
            name='review_date',
            field=models.DateField(auto_now_add=True, verbose_name="today's date"),
        ),
    ]
