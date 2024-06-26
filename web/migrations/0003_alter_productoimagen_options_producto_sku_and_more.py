# Generated by Django 5.0.3 on 2024-03-26 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_productoimagen'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productoimagen',
            options={'verbose_name': 'Imagen del Producto', 'verbose_name_plural': 'Imagenes del Producto'},
        ),
        migrations.AddField(
            model_name='producto',
            name='sku',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='nombre',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
