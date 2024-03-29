# Generated by Django 4.2 on 2023-08-12 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agmcms', '0002_agmprograms_program_attached_file_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='AGMPreviousExhibitionAndCompanyImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/agm/')),
                ('type', models.CharField(choices=[('exhibition', 'exhibition'), ('company', 'company')], max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'AGM previouse exhibition and company image',
                'verbose_name_plural': 'AGM previous exhibition and company images',
            },
        ),
        migrations.DeleteModel(
            name='AGMPreviousExhibitionCompaniesImages',
        ),
        migrations.DeleteModel(
            name='AGMPreviousExhibitionImages',
        ),
        migrations.AlterModelOptions(
            name='agmprograms',
            options={'ordering': ['created_at'], 'verbose_name': 'AGM Program', 'verbose_name_plural': 'AGM Programs'},
        ),
        migrations.AlterField(
            model_name='agmspeakers',
            name='extra_title',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='agmspeakers',
            name='speaker_title',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
