# Generated by Django 4.2 on 2023-06-02 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0008_quickregistration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agminvitation',
            name='type',
            field=models.CharField(choices=[('guest', 'guest'), ('media', 'media'), ('staff', 'staff')], max_length=200),
        ),
    ]
