# Generated by Django 5.1.2 on 2024-10-30 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('edad', models.IntegerField()),
                ('Hobbie', models.CharField(max_length=100)),
                ('documento', models.CharField(choices=[('DNI', 'DNI'), ('Pasaporte', 'Pasaporte')], default='DNI', max_length=9, unique=True)),
            ],
        ),
    ]
