from django.db import models

# Create your models here.

class Persona(models.Model):
    GENEROS = (
        ('M', 'Mascuilino',),
        ('F', 'Femenino',),
        ('N', 'Inseguro',),
    )
    TIPO_IDENT = (
        ('Cedula', 'Cedula',),
        ('RUC', 'RUC',),
        ('Pasaporte', 'Passaporte',),
    )

    name = models.CharField(max_length=500, verbose_name='Nombres')
    genero = models.CharField(default='',max_length=1,choices=GENEROS)
    identificacion = models.CharField(max_length=10, verbose_name='Identificacion')
    tipo_identificacion = models.CharField(default='',max_length=20,choices=TIPO_IDENT)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Persona'
        ordering = ('id',)

class Cliente(Persona):
    ESTADOS_C = (
        ('Soltero', 'Soltero',),
        ('Casado', 'Casado',),
        ('Viudo', 'Viudo',),
        ('Divorciado', 'Divorciado',),
        ('Separado', 'Separado',),
    )
    TIPO_CLI = (
        ('A', 'A',),
        ('B', 'B',),
        ('C', 'C',),
    )

    num_cargas_faml = models.PositiveIntegerField(verbose_name='Numero Cargas Familiares')
    fecha_residencia = models.DateField(verbose_name='Fecha residencia')
    estado_civil = models.CharField(default='',max_length=15,choices=ESTADOS_C)
    tipo_cliente = models.CharField(default='',max_length=1,choices=TIPO_CLI)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ('id',)