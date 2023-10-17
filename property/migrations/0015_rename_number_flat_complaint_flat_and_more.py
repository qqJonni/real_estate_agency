# Generated by Django 4.2.6 on 2023-10-11 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("property", "0014_remove_complaint_like"),
    ]

    operations = [
        migrations.RenameField(
            model_name="complaint",
            old_name="number_flat",
            new_name="flat",
        ),
        migrations.RenameField(
            model_name="owner",
            old_name="owner_pure_phone_number",
            new_name="pure_phone",
        ),
        migrations.RemoveField(
            model_name="owner",
            name="flat_in_owner",
        ),
        migrations.AddField(
            model_name="owner",
            name="flats",
            field=models.ManyToManyField(
                related_name="owners_flats",
                to="property.flat",
                verbose_name="Квартиры в собственности",
            ),
        ),
    ]