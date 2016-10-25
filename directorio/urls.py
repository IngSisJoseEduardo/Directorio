from django.conf.urls import url
from django.contrib import admin

from directorio import views

urlpatterns = [
    url(r'^$',views.home, name = 'home'),
    url(r'^nuevo/$',views.create_directorio, name = "create_dir"),
    url(r'^milista/$',views.milista_dir, name = "milista_dir"),
    url(r'^generar_acuses_milista/$',views.seleccionar_acuses_mi_lista, name="acuses_dir"),
    url(r'^(?P<id>\d+)/editar/$',views.edit_directorio, name = "edit_dir"),
    url(r'^(?P<id>\d+)/detalle/$',views.detail_directorio, name = "detail_dir"),
    url(r'^(?P<id>\d+)/eliminar/$',views.confirm_delete_directorio, name = "confirm_dir"),
    url(r'^(?P<id>\d+)/delete/$',views.delete_directorio, name = "delete_dir"),
    url(r'^(?P<id>\d+)/acuses/$',views.un_acuse, name = 'doc'),
    url(r'^crear_lista/$',views.crear_mi_lista,name = "lista_dir"),
    url(r'^crear_mis_acuses/$',views.crear_mis_acuses, name = 'crear_mis_acuses'),
    url(r'^crear_lista_general',views.crear_lista_general, name = 'crear_lista_general'),
    url(r'^acuses_generales/$',views.acuses_generales,name='acuses_generales'),
    url(r'^generar_acuses_directorio',views.seleccionar_acuses_directorio, name = "seleccion_gral_dir"),
    url(r'^(?P<id>\d+)/load_detail/$',views.load_detail, name ="load_detail"),
]
