# Generated by Django 4.0.5 on 2022-06-23 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='measure_date',
            field=models.DateField(auto_now=True),
        ),
    ]