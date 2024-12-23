# Generated by Django 5.1 on 2024-12-19 16:06

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=25)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("password", models.CharField(max_length=25)),
            ],
        ),
    ]
