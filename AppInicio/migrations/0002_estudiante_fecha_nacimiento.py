# Generated by Django 5.0.6 on 2024-05-17 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppInicio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudiante',
            name='fecha_nacimiento',
            field=models.DateField(null=True, verbose_name='Fecha de nacimiento'),
        ),
    ]