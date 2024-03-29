# Generated by Django 5.0.1 on 2024-01-28 13:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="type",
            field=models.CharField(
                choices=[
                    ("MU", "Музыка"),
                    ("PO", "Политика"),
                    ("ED", "Учеба"),
                    ("DA", "Танцы"),
                    ("AR", "Рисование"),
                    ("PC", "Компьютеры"),
                    ("EA", "Еда"),
                    ("CA", "Машины"),
                ],
                default="C",
                max_length=2,
            ),
        ),
    ]
