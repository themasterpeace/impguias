# Generated by Django 3.2.15 on 2023-01-13 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0005_alter_empleado_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='fotos/'),
        ),
    ]
