# Generated by Django 2.2.24 on 2021-11-15 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_auto_20211114_2234'),
    ]

    operations = [
        migrations.AddField(
            model_name='reason',
            name='name',
            field=models.CharField(default=1, max_length=60),
            preserve_default=False,
        ),
    ]