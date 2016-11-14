from django import template

register = template.Library()

@register.simple_tag
def dir_profesion(directorio, i):
    return ("%s")%directorio[i].profesion

@register.simple_tag
def dir_nombre(directorio, i):
    return directorio[i].nombre

@register.simple_tag
def dir_cargo(directorio, i):
    return ("%s")%directorio[i].cargo

@register.simple_tag
def dir_direccion(directorio, i):
    return ("%s")%directorio[i].direccion
