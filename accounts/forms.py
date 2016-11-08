from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,

    ) 

User = get_user_model()

class UserLoginForm(forms.Form):
    # TODO: Define form fields here
    username = forms.CharField(label = "Usuario")
    password = forms.CharField(widget=forms.PasswordInput,label = 'Contraseña')

    def clean(self,*args,**kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        
        if username and password:
            user = authenticate(username = username,password = password)
            if not user:
                raise forms.ValidationError("Este usuario no existe")
            if not user.check_password(password):
                raise forms.ValidationError("Password incorrecto")
            if not user.is_active:
                raise forms.ValidationError("Este usuario no esta activado")
        return super(UserLoginForm,self).clean(*args,**kwargs)


class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput,label = 'Contraseña')
    confirmpass = forms.CharField(widget=forms.PasswordInput, label = "Confirmar Contraseña")
    #email2 = forms.EmailField(label = "Confirmar correo electronico")
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'password',
            'confirmpass',
            'email',
        ]

    def clean_confirmpass(self):
        password = self.cleaned_data.get('password')
        confirmpass = self.cleaned_data.get('confirmpass')

        print(password, confirmpass)
        if password != confirmpass:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return confirmpass