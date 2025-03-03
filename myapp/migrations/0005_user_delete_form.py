# Generated by Django 5.1.6 on 2025-03-03 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0004_delete_blogpost"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("lname", models.CharField(max_length=100)),
                ("age", models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name="Form",
        ),
    ]
