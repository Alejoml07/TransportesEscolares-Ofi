# Generated by Django 4.0.6 on 2022-11-21 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transportesEscolaresSena', '0005_alter_cliente_rol_alter_vehiculo_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiculo',
            name='color',
            field=models.CharField(max_length=250),
        ),
    ]
