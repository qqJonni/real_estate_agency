# Generated by Django 4.2.6 on 2023-10-10 07:39

from django.db import migrations, IntegrityError


def owner_create(apps, schema_editor):
    Owner = apps.get_model('property', 'Owner')
    Flat = apps.get_model('property', 'Flat')

    try:
        flats = Flat.objects.all().iterator()
        for flat in flats:
            obj, created = Owner.objects.get_or_create(full_name=flat.owner,
                                                       phone_number_owner=flat.owners_phonenumber,
                                                       owner_pure_phone_number=flat.owner_pure_phone,
                                                       )
            obj.flat_in_owner.add(flat)
    except IntegrityError:
        pass
    

class Migration(migrations.Migration):

    dependencies = [
        ("property", "0011_alter_owner_owner_pure_phone_number"),
    ]

    operations = [
        migrations.RunPython(owner_create)
    ]

