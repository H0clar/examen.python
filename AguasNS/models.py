

from django.db import models

class Cliente(models.Model):
    rut = models.CharField(max_length=20)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    sector = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    tipo_usuario = models.CharField(max_length=20, choices=[('Cliente', 'Cliente'), ('Funcionario', 'Funcionario')])

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
