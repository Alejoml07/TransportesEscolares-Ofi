# Generated by Django 4.0.6 on 2022-12-05 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transportesEscolaresSena', '0010_cliente_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='fecha_nacimiento',
            field=models.DateField(),
        ),
    ]
