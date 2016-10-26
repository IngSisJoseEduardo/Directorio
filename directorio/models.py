from django.conf import settings
from django.db import models
from django.core.urlresolvers import reverse


# Create your models here.
class Directorio(models.Model):
    profesion  = models.CharField(max_length=50,null=True,blank=True)
    nombre     = models.CharField(max_length=150)
    pareja     = models.CharField(max_length=150,null=True,blank=True)
    cargo      = models.TextField(null=True,blank=True)
    direccion  = models.TextField(null=True,blank=True)
    telefono   = models.CharField(max_length=50,null=True,blank=True)
    user       = models.ForeignKey(settings.AUTH_USER_MODEL,null=True)
    status     = models.CharField(max_length=1,default='1')
    modificado = models.CharField(max_length=150,null=True)


    class Meta:
        verbose_name = "Directorio"
        verbose_name_plural = "Directorios"

    def __str__(self):
        return "%s%s"%(self.profesion,self.nombre)

    def get_detail_path(self):
        return reverse("directorio:detail_dir",kwargs = {'id':self.id})

class Obsequio(models.Model):
    nombre    = models.CharField(max_length=150)
    cantidad  = models.IntegerField()
    entregado = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name = "Obsequio"
        verbose_name_plural = "Obsequios"

    def __str__(self):
        return self.nombre
    