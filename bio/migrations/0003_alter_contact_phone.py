# Generated by Django 4.2.5 on 2023-09-22 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bio', '0002_alter_contact_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(max_length=13),
        ),
    ]
