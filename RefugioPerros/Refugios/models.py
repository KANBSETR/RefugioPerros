from django.db import models

class Refugio(models.Model):
    id_refugio = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=12)
    email = models.EmailField()
    descripcion = models.TextField()
    fecha_registro = models.DateField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Refugio"
        verbose_name_plural = "Refugios"
        
    def __str__(self):
        return self.nombre
