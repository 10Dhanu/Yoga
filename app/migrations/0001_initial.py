# Generated by Django 4.2.16 on 2024-11-17 20:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="YogaClass",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("schedule", models.DateTimeField()),
                ("instructor", models.CharField(max_length=100)),
                ("capacity", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Booking",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("user_name", models.CharField(max_length=100)),
                ("user_email", models.EmailField(max_length=254)),
                ("booking_date", models.DateTimeField(auto_now_add=True)),
                (
                    "yoga_class",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.yogaclass"
                    ),
                ),
            ],
        ),
    ]
