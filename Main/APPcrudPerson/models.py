from django.db import models

class Persona(models.Model):
    id = models.AutoField(primary_key=True)   
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    hobbie = models.CharField(max_length=100)

    TIPO_DOCUMENTO = [
        ('DNI', 'DNI'),
        ('Pasaporte', 'Pasaporte'),
    ]
    tipo_documento = models.CharField(max_length=10, choices=TIPO_DOCUMENTO, default='DNI')
    numero_documento = models.IntegerField(unique=True)

    def __str__(self):
        return f'{self.apellido}, {self.nombre}, DNI: {self.numero_documento}'
