# Generated by Django 2.2.5 on 2021-11-18 04:12

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('songs', models.CharField(max_length=500)),
                ('year', models.IntegerField()),
                ('image', models.CharField(max_length=500)),
            ],
            managers=[
                ('Songs', django.db.models.manager.Manager()),
            ],
        ),
    ]