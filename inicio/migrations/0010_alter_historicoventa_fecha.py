# Generated by Django 5.0.1 on 2024-02-09 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0009_remove_historicoventa_producto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicoventa',
            name='Fecha',
            field=models.DateField(null=True),
        ),
    ]