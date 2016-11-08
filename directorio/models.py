from django.conf import settings
from django.db import models
from django.core.urlresolvers import reverse


# Create your models here.
class Directorio(models.Model):
    profesion  = models.CharField(max_length=50,null=True,blank=True)
    nombre     = models.CharField(max_length=150,unique=True)
    pareja     = models.CharField(max_length=150,null=True,blank=True)
    cargo      = models.TextField(null=True,blank=True)
    direccion  = models.TextField(null=True,blank=True)
    telefono   = models.CharField(max_length=50,null=True,blank=True)
    user       = models.ForeignKey(settings.AUTH_USER_MODEL,null=True,blank=True)
    status     = models.CharField(max_length=1,default='1')
    modificado = models.CharField(max_length=150,null=True,blank=True)
    cdmx       = models.BooleanField(default=False)



    class Meta:
        verbose_name = "Directorio"
        verbose_name_plural = "Directorios"

    def __str__(self):
        return "%s%s"%(self.profesion,self.nombre)

    def get_detail_path(self):
        return reverse("directorio:detail_dir",kwargs = {'id':self.id})

    

class Obsequio(models.Model):
    nombre     = models.CharField(max_length=150)
    cantidad   = models.IntegerField()
    entregado  = models.IntegerField(default=0,null=True, blank=True)
    existencia = models.IntegerField(default=0,null=True,blank=True)
    default    = models.BooleanField(default=False)
    timestamps = models.DateTimeField(auto_now=True,auto_now_add=False)


    class Meta:
        verbose_name = "Obsequio"
        verbose_name_plural = "Obsequios"

    def __str__(self):
        return self.nombre

class Historial(models.Model):
    directorio = models.ForeignKey(Directorio)
    obsequio   = models.ForeignKey(Obsequio)
    timestamps = models.DateTimeField(auto_now=True,auto_now_add=False)
    class Meta:
        verbose_name = "Historial"
        verbose_name_plural = "Historiales"

    def __str__(self):
        return self.directorio.nombre

class Acuse(models.Model):
    contenido  = models.TextField()
    update     = models.DateTimeField(auto_now=True,auto_now_add=False)
    timestamps = models.DateTimeField(auto_now=False,auto_now_add=True)
    obsequio   = models.OneToOneField(Obsequio)
    default     = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Acuse"
        verbose_name_plural = "Acuses"

    def __str__(self):
        return self.contenido
    