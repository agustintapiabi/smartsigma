# Generated by Django 5.0.1 on 2024-02-05 04:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0006_historicoventa'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='historicoventa',
            table='ventas',
        ),
    ]
