from django.db import models

class Parroquia(models.Model):
    UBICACIONES = [
        ('norte', 'Norte'),
        ('sur', 'Sur'),
        ('este', 'Este'),
        ('oeste', 'Oeste'),
    ]
    TIPOS = [
        ('urbana', 'Urbana'),
        ('rural', 'Rural'),
    ]

    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=10, choices=UBICACIONES)
    tipo = models.CharField(max_length=10, choices=TIPOS)

    def __str__(self):
        return self.nombre

class Barrio(models.Model):
    nombre = models.CharField(max_length=100)
    numero_viviendas = models.IntegerField()
    numero_parques = models.IntegerField(choices=[(i, str(i)) for i in range(1, 7)])
    numero_edificios_residenciales = models.IntegerField()
    parroquia = models.ForeignKey(Parroquia, on_delete=models.CASCADE, related_name='barrios')

    def __str__(self):
        return self.nombre
