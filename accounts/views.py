from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,

    )
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserLoginForm, UserRegisterForm
from django.http import HttpResponse, HttpResponseRedirect



def login_view(request):
    if request.user.is_authenticated():
        return redirect('directorio:home')

    next = request.GET.get("next")
    title = "Iniciar Sesión"
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get('password')

        user = authenticate(username = username,password = password)
        login(request,user)
        if next:
            return redirect(next)
        return redirect('directorio:home')
    return render(request,"form.html",{"form" : form,"title":title})


def register_view(request):
    title = "Usuario Nuevo"
    form = UserRegisterForm(request.POST or None)

    if form.is_valid():
        user = form.save(commit = False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()

        new_user = authenticate(username = user.username, password = password)
        login(request,new_user)
        return redirect('directorio:home')

    contexto = {
        "form" : form,
        "title" : title
    }
    return render(request,"form.html",contexto)

@login_required
def update_user(request, id = None):
    user_perfil = get_object_or_404(User,id = id)
    if request.POST:
        user_perfil.first_name = request.POST.get("nombre")
        user_perfil.last_name = request.POST.get("apellidos")
        user_perfil.save()
        return redirect("directorio:user_perfil")

    contexto = {
        "user": user_perfil
    }
    return render(request,"perfil.html",contexto)

def edit_password(request,id = None):
    user_password = get_object_or_404(User, id = id)

    if request.POST:
        if user_password.check_password(request.POST.get("password")):
            if request.POST.get("new_password") == request.POST.get("confirm_password"):
                user_password.set_password(request.POST.get("new_password"))
                user_password.save()
                return redirect("directorio:user_perfil")
            else:
                print("no coinciden")
        else:
            print("son distintas")
    return render(request,'edit_password.html')


def logout_view(request):
    logout(request)
    return redirect('accounts:login')