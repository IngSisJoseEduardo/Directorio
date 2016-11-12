from django import template

register = template.Library()

@register.simple_tag
def dir_profesion(directorio, i):
    print(i)
    return ("%s")%directorio[i].profesion

@register.simple_tag
def dir_nombre(directorio, i):
    print(i)
    return ("%s")%directorio[i].nombre

@register.simple_tag
def dir_cargo(directorio, i):
    print(i)
    return ("%s")%directorio[i].cargo

@register.simple_tag
def dir_direccion(directorio, i):
    print(i)
    return ("%s")%directorio[i].direccion

@register.simple_tag
def condicion(i,lista):
    if i < len(lista):
        return True
    else:
        return False