# Generated by Django 4.1.7 on 2023-12-16 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0002_class_capacity'),
    ]

    operations = [
        migrations.AddField(
            model_name='year',
            name='students',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
