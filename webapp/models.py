from django.db import models

# Create your models here.
class Cliente(models.Model):
    rut = models.CharField(max_length=10)
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    telefono = models.CharField(max_length=11)
    mail = models.CharField(max_length=30)
    direccion = models.CharField(max_length=40)

    def __str__(self):
        return self.nombre +' '+ self.apellido

class Proveedor(models.Model):
    nombre = models.CharField(max_length=40)
    rut = models.CharField(max_length=10)
    direccion = models.CharField(max_length=40)
    telefono = models.CharField(max_length=11)
    mail = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

class Producto_Servicio(models.Model):
    nombre = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=40)    

    def __str__(self):
        return self.nombre

ESTADO_OPCIONES = (
    ("1", "pendiente"),
    ("2", "finalizado"),
    ("3", "desestimado"),
)
      

class Solicitud(models.Model):
    inicio = models.DateTimeField
    fin = models.DateTimeField
    estado = models.CharField(
        max_length = 3,
        choices = ESTADO_OPCIONES,
        default = '1'
        )
    id_proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    id_prod_serv = models.ForeignKey(Producto_Servicio, on_delete=models.CASCADE)

    def __str__(self):
        return 'Solicitud 000' + str(self.id)


class Tecnico(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    rut = models.CharField(max_length=10)
    especialidad = models.CharField(max_length=30)
    telefono = models.CharField(max_length=11)
    id_proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre    
class Protocolo_Mant(models.Model):
    nombre = models.CharField(max_length=40)
    descripcion_prot = models.TextField(max_length=300)
    id_tecnico = models.ForeignKey(Tecnico, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre 
