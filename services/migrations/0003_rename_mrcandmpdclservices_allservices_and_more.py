# Generated by Django 4.2 on 2023-04-10 22:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_mrcandmpdclservices_delete_coreservices_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MRCandMPDCLServices',
            new_name='AllServices',
        ),
        migrations.RenameField(
            model_name='requestservice',
            old_name='firstname',
            new_name='name',
        ),
    ]
