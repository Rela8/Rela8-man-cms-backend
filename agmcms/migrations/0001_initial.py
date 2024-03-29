# Generated by Django 4.2 on 2023-08-08 15:26

import cloudinary_storage.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AGMExhibitionCMS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_image', models.ImageField(blank=True, null=True, upload_to='images/agm/')),
                ('intro_text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'AGM exhibition cms',
                'verbose_name_plural': 'AGM exhibition cms',
            },
        ),
        migrations.CreateModel(
            name='AGMFAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=400)),
                ('content', models.TextField()),
            ],
            options={
                'verbose_name': 'AGM Faq',
                'verbose_name_plural': 'AGM Faqs',
            },
        ),
        migrations.CreateModel(
            name='AGMHomepageCMS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_image', models.ImageField(blank=True, null=True, upload_to='images/agm/')),
                ('intro_text', models.TextField()),
                ('location', models.TextField()),
                ('agm_start_date', models.DateField()),
                ('countdown_text', models.CharField(max_length=300)),
                ('intro_title', models.CharField(max_length=500)),
                ('intro_description', models.TextField()),
                ('exhibition_text', models.CharField(max_length=300)),
                ('exhibition_image', models.ImageField(blank=True, null=True, upload_to='images/agm/')),
                ('save_date_text', models.CharField(max_length=300)),
                ('save_date_image', models.ImageField(blank=True, null=True, upload_to='images/agm/')),
                ('venue_text', models.CharField(max_length=300)),
                ('venue_text_image', models.ImageField(blank=True, null=True, upload_to='images/agm/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'AGM homepage cms',
                'verbose_name_plural': 'AGM homepage cms',
            },
        ),
        migrations.CreateModel(
            name='AGMPreviousExhibitionCompaniesImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/agm/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'AGM previouse exhibition company image',
                'verbose_name_plural': 'AGM previous exhibition companies images',
            },
        ),
        migrations.CreateModel(
            name='AGMPreviousExhibitionImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/agm/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'AGM previouse exhibition image',
                'verbose_name_plural': 'AGM previous exhibition images',
            },
        ),
        migrations.CreateModel(
            name='AGMProgrammeCMS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_image', models.ImageField(blank=True, null=True, upload_to='images/agm/')),
                ('main_text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'AGM programme cms',
                'verbose_name_plural': 'AGM programme cms',
            },
        ),
        migrations.CreateModel(
            name='AGMPrograms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('program_date', models.DateField()),
                ('program_title', models.CharField(unique=True)),
                ('program_attached_file1', models.FileField(blank=True, null=True, storage=cloudinary_storage.storage.RawMediaCloudinaryStorage, upload_to='')),
                ('program_attached_file2', models.FileField(blank=True, null=True, storage=cloudinary_storage.storage.RawMediaCloudinaryStorage, upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'AGM Program',
                'verbose_name_plural': 'AGM Programs',
            },
        ),
        migrations.CreateModel(
            name='AGMSpeakers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intro_text', models.CharField(max_length=300)),
                ('header', models.CharField(max_length=300)),
                ('speaker_title', models.CharField(max_length=300)),
                ('speaker_name', models.CharField(max_length=300)),
                ('extra_title', models.CharField(max_length=300)),
                ('speaker_image', models.ImageField(blank=True, null=True, upload_to='images/agm/')),
                ('speaker_words', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'AGM Speaker',
                'verbose_name_plural': 'AGM Speakers',
            },
        ),
        migrations.CreateModel(
            name='AGMVenue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('venue_image', models.ImageField(blank=True, null=True, upload_to='images/agm/')),
                ('venue_location_text', models.TextField()),
                ('venue_location_map', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'AGM Venue',
                'verbose_name_plural': 'AGM Venues',
            },
        ),
    ]
