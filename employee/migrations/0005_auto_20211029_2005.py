# Generated by Django 2.2.24 on 2021-10-30 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0004_auto_20211028_2037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requirements',
            name='date_end',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='requirements',
            name='date_start',
            field=models.DateField(),
        ),
    ]
