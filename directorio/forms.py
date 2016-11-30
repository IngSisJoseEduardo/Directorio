from django import forms
from directorio.models import Directorio

class DirectorioForm(forms.ModelForm):
    profesion = forms.CharField(max_length=50,label='Profesión',required=False)
    pareja    = forms.CharField(max_length=150,label='Esposa(o)',required=False)
    # acuse = forms.ChoiceField(label="Acuse",required=True)
    # cdmx      = forms.BooleanField(label='CDMX',required=False)
    # opciones para el select de status
    status_opcion = (
        ('1','No Autorizado'),
        ('2','Autorizado'),
        ('3','Entregado')
    )
    status = forms.ChoiceField(choices=status_opcion,required=True)
    class Meta:
        model = Directorio
        fields = [
            'profesion',
            'nombre',
            'acuse',
            'pareja',
            'cargo',
            'direccion',
            'telefono',
            'status',
            # 'cdmx',
        ]