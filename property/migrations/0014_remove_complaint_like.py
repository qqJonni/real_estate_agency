# Generated by Django 4.2.6 on 2023-10-11 05:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("property", "0013_remove_flat_owner_remove_flat_owner_pure_phone_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="complaint",
            name="like",
        ),
    ]