# Generated by Django 5.1.2 on 2024-10-30 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APPcrudPerson', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='persona',
            name='documento',
        ),
        migrations.AddField(
            model_name='persona',
            name='numero_documento',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='persona',
            name='tipo_documento',
            field=models.CharField(choices=[('DNI', 'DNI'), ('Pasaporte', 'Pasaporte')], default='DNI', max_length=10, unique=True),
        ),
    ]
