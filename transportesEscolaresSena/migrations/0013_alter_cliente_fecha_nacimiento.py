# Generated by Django 4.0.6 on 2022-12-05 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transportesEscolaresSena', '0012_alter_cliente_fecha_nacimiento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='fecha_nacimiento',
            field=models.DateField(),
        ),
    ]
