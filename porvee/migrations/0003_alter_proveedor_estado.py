# Generated by Django 3.2.16 on 2023-12-08 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('porvee', '0002_alter_proveedor_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedor',
            name='estado',
            field=models.BooleanField(default=True),
        ),
    ]
