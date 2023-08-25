# Generated by Django 2.2.5 on 2021-05-25 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StockTrading', '0005_auto_20210524_2059'),
    ]

    operations = [
        migrations.RenameField(
            model_name='story',
            old_name='lName',
            new_name='last_name',
        ),
        migrations.AlterField(
            model_name='story',
            name='tags',
            field=models.CharField(blank=True, choices=[('Programming', 'Programming'), ('Strategy', 'Strategy'), ('Algorithms', 'Algorithms')], max_length=50),
        ),
    ]