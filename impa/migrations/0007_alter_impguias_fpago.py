# Generated by Django 4.2.8 on 2023-12-27 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('impa', '0006_alter_impguias_fpago'),
    ]

    operations = [
        migrations.AlterField(
            model_name='impguias',
            name='fpago',
            field=models.CharField(max_length=20, verbose_name='FORMA DE PAGO'),
        ),
    ]
