# Generated by Django 2.2.5 on 2021-06-28 17:42

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
            ],
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=50)),
                ('Details', models.TextField(blank=True, default='', max_length=300)),
                ('Priority', models.CharField(choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')], default='', max_length=50)),
                ('Category', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='NoteTaking.Categorie')),
            ],
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]