# Generated by Django 3.0.5 on 2020-05-11 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0002_auto_20200511_1025'),
    ]

    operations = [
        migrations.AddField(
            model_name='title',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]