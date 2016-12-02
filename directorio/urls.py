from django.conf.urls import url
from django.contrib import admin

from directorio import views
from accounts.views import update_user, edit_password

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
    url(r'^informacion/$',views.informacion2, name = "informacion"),
    url(r'^eliminado/$',views.eliminado, name = 'eliminado'),
    url(r'^agregar/(?P<id>\d+)/',views.agregar_mi_lista, name = "agregar"),
    url(r'^quitar/(?P<id>\d+)/',views.quitar_mi_lista, name = "quitar"),

    #configurcion y perfil del usuario
    url(r'^perfil/$',views.config_user, name = "user_perfil"),
    url(r'^perfil/(?P<id>\d+)/config',update_user, name = "config_perfil"),
    url(r'^perfil/(?P<id>\d+)/password', edit_password, name = "edit_password"),
    
    # Vistas de acuse
    url(r'^acuses/$',views.acuses_lista, name = "acuses_lista"),
    url(r'^nuevo/acuse',views.nuevo_acuse, name ="nuevo_acuse"),
    url(r'^(?P<id>\d+)/editar_acuse/$',views.editar_acuse, name = 'editar_acuse'),
    url(r'^ver_acuse/$',views.ver_acuse,name = 'ver_acuse'),

    #vistas de etiquetas
    url(r'^(?P<id>\d+)/etiqueta/$',views.una_etiqueta, name = "una_etiqueta"),
    url(r'^all_etiquetas/$',views.all_etiquetas, name ="all_etiquetas"),
    url(r'^mis_etiquetas',views.mis_etiquetas, name = "mis_etiquetas"),

    #control de llibros
    url(r'^obsequios/$',views.control_obsequios, name ="control_obsequios"),
    url(r'^nuevo/obsequio$',views.new_obsequio, name = "new_obsequio"),
    url(r'^editar/obsequio/(?P<id>\d+)$',views.editar_obsequio, name = "editar_obsequio"),
    url(r'^agregar/entregados',views.agregar_entregados, name = "agregar_entregados"),
]
