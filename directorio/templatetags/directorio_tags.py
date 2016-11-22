from django.utils.safestring import mark_safe
from django.utils.html import escape
from django import template

register = template.Library()

@register.simple_tag
def dir_profesion(directorio, i):
    return ("%s")%directorio[i].profesion

@register.simple_tag
def dir_nombre(directorio, i):
    value = directorio[i].nombre
    if directorio[i].pareja:
        value+="\ny "
        value+= directorio[i].pareja
    return wordlinebreaks(value)

@register.simple_tag
def dir_etiqueta(directorio, i):
    value = ""
    if directorio[i].cargo:
        value+= directorio[i].cargo
        value+= "\n"
    if directorio[i].cargo != None:
        value += directorio[i].direccion
    return wordlinebreaks(value)

def wordlinebreaks(value):
    paragraphs = [line for line in escape(value).splitlines()]
    return mark_safe('<text:line-break/>'.join(paragraphs))