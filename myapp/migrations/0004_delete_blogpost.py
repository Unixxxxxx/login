# Generated by Django 5.1.6 on 2025-02-19 06:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0003_blogpost"),
    ]

    operations = [
        migrations.DeleteModel(
            name="BlogPost",
        ),
    ]
