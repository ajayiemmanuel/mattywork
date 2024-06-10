# Generated by Django 5.0.6 on 2024-06-10 08:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('broker', '0018_report'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transactionone',
            name='user',
        ),
        migrations.RemoveField(
            model_name='transactionthree',
            name='user',
        ),
        migrations.RemoveField(
            model_name='transactiontwo',
            name='user',
        ),
        migrations.CreateModel(
            name='Banktransfer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('transaction', models.CharField(blank=True, max_length=250, null=True)),
                ('bank', models.CharField(blank=True, max_length=254, null=True)),
                ('accountnumber', models.CharField(blank=True, max_length=254, null=True)),
                ('gateway', models.CharField(blank=True, max_length=254, null=True)),
                ('swift', models.CharField(blank=True, max_length=254, null=True)),
                ('amount', models.CharField(blank=True, default='$10', max_length=250, null=True)),
                ('charge', models.CharField(blank=True, default='pending', max_length=250, null=True)),
                ('status', models.CharField(blank=True, max_length=250, null=True)),
                ('time', models.DateField(auto_now=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Banktransfer',
                'verbose_name_plural': 'Banktransfers',
            },
        ),
        migrations.CreateModel(
            name='Bitcoin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction', models.CharField(blank=True, max_length=250, null=True)),
                ('wallet', models.CharField(blank=True, max_length=250, null=True)),
                ('gateway', models.CharField(blank=True, max_length=254, null=True)),
                ('charge', models.CharField(blank=True, default='pending', max_length=250, null=True)),
                ('time', models.DateField(auto_now=True)),
                ('name', models.CharField(max_length=200, null=True)),
                ('number', models.CharField(default='4', max_length=200)),
                ('tf_type', models.CharField(default='-', max_length=200)),
                ('amount', models.CharField(default='-', max_length=200)),
                ('status', models.CharField(default='-', max_length=200)),
                ('date_time', models.CharField(default='-', max_length=200)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Bitcoin',
                'verbose_name_plural': 'Bitcoins',
            },
        ),
        migrations.CreateModel(
            name='Wiretransfer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('transaction', models.CharField(blank=True, max_length=250, null=True)),
                ('bank', models.CharField(blank=True, max_length=254, null=True)),
                ('accountnumber', models.CharField(blank=True, max_length=254, null=True)),
                ('gateway', models.CharField(blank=True, max_length=254, null=True)),
                ('swift', models.CharField(blank=True, max_length=254, null=True)),
                ('amount', models.CharField(blank=True, default='$10', max_length=250, null=True)),
                ('charge', models.CharField(blank=True, default='pending', max_length=250, null=True)),
                ('status', models.CharField(blank=True, max_length=250, null=True)),
                ('time', models.DateField(auto_now=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Wiretransfer',
                'verbose_name_plural': 'Wiretransfers',
            },
        ),
        migrations.DeleteModel(
            name='Transaction',
        ),
        migrations.DeleteModel(
            name='Transactionone',
        ),
        migrations.DeleteModel(
            name='Transactionthree',
        ),
        migrations.DeleteModel(
            name='Transactiontwo',
        ),
    ]