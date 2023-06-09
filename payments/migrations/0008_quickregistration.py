# Generated by Django 4.2 on 2023-05-18 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0007_agminvitation_company_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuickRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=300)),
                ('designation', models.CharField(max_length=300)),
                ('name', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=254)),
                ('phone_no', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
