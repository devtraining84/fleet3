# Generated by Django 3.2.12 on 2022-07-06 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0009_auto_20220706_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drivercertificatesmodel',
            name='ADR_data_konc',
            field=models.DateField(blank=True, null=True, verbose_name='ADR data koncowa'),
        ),
        migrations.AlterField(
            model_name='drivercertificatesmodel',
            name='driver_licence_enddate',
            field=models.DateField(blank=True, null=True, verbose_name='Prawo Jazdy data koncowa'),
        ),
        migrations.AlterField(
            model_name='drivercertificatesmodel',
            name='kwalifikacja_data_konc',
            field=models.DateField(blank=True, null=True, verbose_name='Swiadectwo kwal. data koncowa'),
        ),
    ]
