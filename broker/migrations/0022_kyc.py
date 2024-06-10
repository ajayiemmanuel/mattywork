# Generated by Django 5.0.6 on 2024-06-10 11:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('broker', '0021_alter_account_account_name_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Kyc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200, null=True)),
                ('last_name', models.CharField(blank=True, max_length=250, null=True)),
                ('email', models.CharField(blank=True, max_length=250, null=True)),
                ('gender', models.CharField(blank=True, max_length=254, null=True)),
                ('country_code', models.CharField(blank=True, default='$10', max_length=250, null=True)),
                ('country', models.CharField(blank=True, default='pending', max_length=250, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=250, null=True)),
                ('year', models.CharField(blank=True, max_length=250, null=True)),
                ('month', models.CharField(blank=True, max_length=250, null=True)),
                ('day', models.CharField(blank=True, max_length=250, null=True)),
                ('valid_id_front', models.ImageField(blank=True, null=True, upload_to='')),
                ('valid_id_back', models.ImageField(blank=True, null=True, upload_to='')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Kyc',
                'verbose_name_plural': 'Kycs',
            },
        ),
    ]
