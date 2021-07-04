# Generated by Django 3.2 on 2021-06-23 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_advert_delete_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advert',
            name='days',
            field=models.CharField(choices=[('day3', 3), ('day7', 7), ('day10', 10)], max_length=20),
        ),
    ]