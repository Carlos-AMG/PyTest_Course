# Generated by Django 4.2.2 on 2023-06-13 18:13

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("companies", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="company",
            old_name="aplication_link",
            new_name="application_link",
        ),
    ]