# Generated by Django 4.2 on 2023-05-22 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('publication_news', 'publication_news'), ('event_training', 'event_training'), ('public_view', 'public_view'), ('registrations_payments', 'registrations_payments'), ('prospective_certificates', 'prospective_certificates'), ('super_user', 'super_user')], default='super_user', max_length=200),
            preserve_default=False,
        ),
    ]