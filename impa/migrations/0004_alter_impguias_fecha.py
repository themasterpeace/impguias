# Generated by Django 4.2.8 on 2023-12-27 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('impa', '0003_alter_impguias_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='impguias',
            name='fecha',
            field=models.DateTimeField(),
        ),
    ]
