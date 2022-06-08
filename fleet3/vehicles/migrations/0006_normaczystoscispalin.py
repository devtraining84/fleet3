# Generated by Django 3.2.12 on 2022-06-08 11:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0005_adr'),
    ]

    operations = [
        migrations.CreateModel(
            name='NormaCzystosciSpalin',
            fields=[
                ('norma', models.CharField(choices=[('Euro 7', 'Euro 7'), ('Euro 6', 'Euro 6'), ('Euro 5', 'Euro 5'), ('Euro 4', 'Euro 4'), ('Euro 3', 'Euro 3'), ('Euro 2', 'Euro 2'), ('Euro 1', 'Euro 1'), ('Euro 0', 'Euro 0'), ('N49', 'N49'), ('nie dotyczy', 'nie dotyczy')], default='nie dotyczy', max_length=12, null=True)),
                ('wymagane', models.BooleanField(default=False)),
                ('pojazd', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='normaeuro', serialize=False, to='vehicles.vehiclesmodel')),
            ],
        ),
    ]
