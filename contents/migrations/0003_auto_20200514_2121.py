# Generated by Django 3.0.5 on 2020-05-14 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0002_auto_20200513_0022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]
