# Generated by Django 4.2.6 on 2023-10-09 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("property", "0007_flat_owner_pure_phone_alter_complaint_id_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="flat",
            name="active",
            field=models.BooleanField(
                db_index=True, verbose_name="Активно-ли объявление"
            ),
        ),
    ]