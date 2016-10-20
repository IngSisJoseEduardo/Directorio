from django.conf.urls import url
from django.contrib import admin

from directorio.views import (
                                home,
                                create_directorio,
                                edit_directorio, detail_directorio, 
                                confirm_delete_directorio,
                                delete_directorio,
                                milista_dir,
                                un_acuse,
                                seleccionar_acuses,
                                crear_mi_lista,
                                crear_mis_acuses,
                                crear_lista_general,
                                acuses_generales,
                            )

urlpatterns = [
    url(r'^$',home, name = 'home'),
    url(r'^nuevo/$',create_directorio, name = "create_dir"),
    url(r'^milista/$',milista_dir, name = "milista_dir"),
    url(r'^generar_acuses/$',seleccionar_acuses, name="acuses_dir"),
    url(r'^(?P<id>\d+)/editar/$',edit_directorio, name = "edit_dir"),
    url(r'^(?P<id>\d+)/detalle/$',detail_directorio, name = "detail_dir"),
    url(r'^(?P<id>\d+)/eliminar/$',confirm_delete_directorio, name = "confirm_dir"),
    url(r'^(?P<id>\d+)/delete/$',delete_directorio, name = "delete_dir"),
    url(r'^(?P<id>\d+)/acuses/$',un_acuse, name = 'doc'),
    url(r'^crear_lista/$',crear_mi_lista,name = "lista_dir"),
    url(r'^crear_mis_acuses/$',crear_mis_acuses, name = 'crear_mis_acuses'),
    url(r'^crear_lista_general',crear_lista_general, name = 'crear_lista_general'),
    url(r'^acuses_generales/$',acuses_generales,name='acuses_generales'),
]
