# Generated by Django 4.0.6 on 2023-01-18 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transportesEscolaresSena', '0019_alter_vehiculo_cliente'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='foto',
        ),
    ]
