# Generated by Django 3.0.5 on 2020-05-11 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("text", models.TextField(max_length=1000)),
                ("pub_date", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Review",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("text", models.TextField(max_length=10000)),
                (
                    "score",
                    models.IntegerField(
                        choices=[
                            (1, 1),
                            (2, 2),
                            (3, 3),
                            (4, 4),
                            (5, 5),
                            (6, 6),
                            (7, 7),
                            (8, 8),
                            (9, 9),
                            (10, 10),
                        ]
                    ),
                ),
                ("pub_date", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
