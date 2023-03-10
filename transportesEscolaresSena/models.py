from django.db import models

# Create your models here.

class Cliente(models.Model):
    """Cliente de la aplicacion, dividido en 3 roles
    """
    nombre = models.CharField(max_length= 100)
    apellido = models.CharField(max_length= 200)
    correo = models.EmailField(max_length= 250, null=True, blank=True, unique = True)
    direccion = models.CharField(max_length= 100)
    documento = models.IntegerField(unique = True)
    fecha_nacimiento = models.DateField()
    usuario = models.CharField(max_length=100, default = "u1", unique = True)
    clave = models.CharField(max_length=254, default = "12345")
    ROLES = (
        ('A', 'Administrador'),
        ('C', 'Cliente'),
        ('P', 'Proveedor'),
    )
    rol = models.CharField(max_length=100, choices=ROLES, default='C')


    def __str__(self):
        return f" {self.nombre} "

class Beneficiarios (models.Model):
    cliente = models.ForeignKey(Cliente,on_delete = models.DO_NOTHING)
    nombre = models.CharField(max_length= 100)
    apellido = models.CharField(max_length= 100)
    documento = models.IntegerField(unique = True)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return f" {self.nombre} "


class Comentarios (models.Model):
    cliente = models.ForeignKey(Cliente,on_delete = models.DO_NOTHING)
    tipo = models.CharField(max_length= 100)
    desc = models.CharField(max_length= 1000)

    def __str__(self):
        return f"{self.cliente} {self.tipo}"


class Servicios (models.Model):
    nombre = models.CharField(max_length= 100)
    caracteristicas = models.CharField(max_length= 500)

    def __str__(self):
        return f" {self.nombre} "


class Peticiones(models.Model):
    cliente = models.ForeignKey(Cliente,on_delete = models.DO_NOTHING)
    servicios = models.ForeignKey(Servicios,on_delete = models.DO_NOTHING)
    beneficiarios = models.ForeignKey(Beneficiarios,on_delete = models.DO_NOTHING)
    direccion = models.CharField(max_length= 100)
    colegio = models.CharField(max_length= 200)
    horario = models.CharField(max_length= 100)
    estado = models.CharField(max_length= 100, default='Pendiente')
    comentario_add = models.CharField(max_length= 100, null=True,blank=True)

    def __str__(self):
        return f" {self.cliente},{self.servicios} "


class Vehiculo (models.Model):
    placa = models.CharField(max_length= 100, unique = True)
    marca = models.CharField(max_length= 100)
    color = models.CharField(max_length= 250)
    cliente = models.OneToOneField(Cliente,on_delete = models.DO_NOTHING)
    capacidad = models.PositiveIntegerField()
    actual = models.PositiveIntegerField(default=0)

    
    
    def __str__(self):
        return f" {self.cliente},{self.placa} "


