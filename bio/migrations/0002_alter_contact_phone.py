# Generated by Django 4.2.5 on 2023-09-22 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.IntegerField(),
        ),
    ]
