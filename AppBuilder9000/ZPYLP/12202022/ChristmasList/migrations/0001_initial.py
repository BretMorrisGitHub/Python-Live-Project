# Generated by Django 2.2.5 on 2022-11-22 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gift',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('color', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=255)),
            ],
        ),
    ]