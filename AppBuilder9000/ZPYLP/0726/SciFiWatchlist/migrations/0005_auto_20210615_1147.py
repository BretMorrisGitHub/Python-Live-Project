# Generated by Django 2.2.5 on 2021-06-15 15:47

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('SciFiWatchlist', '0004_auto_20210614_1846'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='movie',
            managers=[
                ('Movies', django.db.models.manager.Manager()),
            ],
        ),
    ]