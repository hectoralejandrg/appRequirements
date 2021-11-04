# Generated by Django 2.2.24 on 2021-10-29 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_reason_requirements'),
    ]

    operations = [
        migrations.CreateModel(
            name='Holidays',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_start', models.DateTimeField()),
                ('date_end', models.DateTimeField()),
                ('days', models.DateField()),
            ],
        ),
        migrations.AlterField(
            model_name='requirements',
            name='date_end',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='requirements',
            name='date_start',
            field=models.DateTimeField(),
        ),
    ]