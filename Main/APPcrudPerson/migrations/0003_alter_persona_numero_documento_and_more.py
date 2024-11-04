# Generated by Django 5.1.2 on 2024-11-04 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APPcrudPerson', '0002_remove_persona_documento_persona_numero_documento_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='numero_documento',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='tipo_documento',
            field=models.CharField(choices=[('DNI', 'DNI'), ('Pasaporte', 'Pasaporte')], default='DNI', max_length=10),
        ),
    ]