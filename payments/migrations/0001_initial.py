# Generated by Django 4.2 on 2023-04-30 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('publications', '0007_delete_publicationpayment'),
    ]

    operations = [
        migrations.CreateModel(
            name='PublicationPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref', models.CharField(max_length=300)),
                ('fullname', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=20)),
                ('company_name', models.CharField(max_length=300)),
                ('is_verified', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('publication', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='publications.publication')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
