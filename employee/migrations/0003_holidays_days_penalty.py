# Generated by Django 2.2.24 on 2022-01-05 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_auto_20220105_0216'),
    ]

    operations = [
        migrations.AddField(
            model_name='holidays',
            name='days_penalty',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
