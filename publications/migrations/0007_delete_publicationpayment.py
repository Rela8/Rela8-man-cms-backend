# Generated by Django 4.2 on 2023-04-30 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0006_publicationpayment_delete_publicationparagraph'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PublicationPayment',
        ),
    ]