# Generated by Django 3.2.12 on 2022-07-05 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0007_auto_20220704_1005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drivercertificatesmodel',
            name='ADR_data_konc',
            field=models.DateField(blank=True, verbose_name='ADR data koncowa'),
        ),
        migrations.AlterField(
            model_name='drivercertificatesmodel',
            name='driver_licence_enddate',
            field=models.DateField(blank=True, verbose_name='Prawo Jazdy data koncowa'),
        ),
        migrations.AlterField(
            model_name='drivercertificatesmodel',
            name='kwalifikacja_data_konc',
            field=models.DateField(blank=True, verbose_name='Swiadectwo kwal. data koncowa'),
        ),
    ]
