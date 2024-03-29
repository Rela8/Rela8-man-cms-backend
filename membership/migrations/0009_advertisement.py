# Generated by Django 4.2 on 2023-08-15 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0008_ourmembers_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/advert/')),
                ('text', models.CharField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'advertisment',
                'verbose_name_plural': 'advertisments',
            },
        ),
    ]
