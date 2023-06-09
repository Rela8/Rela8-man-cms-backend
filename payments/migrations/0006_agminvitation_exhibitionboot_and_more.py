# Generated by Django 4.2 on 2023-05-16 14:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0002_rename_is_special_event_is_agm_and_more'),
        ('payments', '0005_agmregistration_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='AGMInvitation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('exhibitor-participant', 'exhibitor-participant'), ('guest', 'guest'), ('media', 'media'), ('staff', 'staff')], max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('is_valid', models.BooleanField(default=True)),
                ('ref', models.CharField(max_length=300)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ExhibitionBoot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('name', models.CharField(max_length=200)),
                ('is_occupied', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ExhibitorsAGMRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=254)),
                ('company_name', models.CharField(max_length=300)),
                ('company_address', models.CharField(max_length=300)),
                ('participant', models.JSONField()),
                ('amount_to_pay', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('luncheon_covered_participants', models.IntegerField(default=0)),
                ('boot', models.JSONField()),
                ('is_verified', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('event', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='events.event')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Luncheon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('member', 'member'), ('exhibitor', 'exhibitor')], max_length=100, unique=True)),
                ('price', models.DecimalField(decimal_places=2, default=10000.0, max_digits=20)),
            ],
        ),
        migrations.CreateModel(
            name='MembersAGMRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=254)),
                ('company_name', models.CharField(max_length=300)),
                ('company_address', models.CharField(max_length=300)),
                ('participant', models.JSONField()),
                ('is_verified', models.BooleanField(default=False)),
                ('amount_to_pay', models.DecimalField(decimal_places=2, max_digits=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('event', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='events.event')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='OthersAGMRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref', models.CharField(max_length=300)),
                ('type', models.CharField(choices=[('exhibitor-participant', 'exhibitor-participant'), ('guest', 'guest'), ('media', 'media'), ('staff', 'staff')], max_length=200)),
                ('company_name', models.CharField(max_length=300)),
                ('designation', models.CharField(max_length=300)),
                ('name', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=254)),
                ('phone_no', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('event', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='events.event')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.AlterField(
            model_name='eventtrainingregistration',
            name='amount_to_pay',
            field=models.DecimalField(decimal_places=2, max_digits=20),
        ),
        migrations.AlterField(
            model_name='publicationpayment',
            name='amount_to_pay',
            field=models.DecimalField(decimal_places=2, max_digits=20),
        ),
        migrations.DeleteModel(
            name='AGMRegistration',
        ),
        migrations.AddField(
            model_name='exhibitionboot',
            name='rented_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='payments.exhibitorsagmregistration'),
        ),
        migrations.AddField(
            model_name='exhibitionboot',
            name='writer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
