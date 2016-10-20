from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,

    )
from django.shortcuts import render, redirect
from .forms import UserLoginForm, UserRegisterForm


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
    title = "Register User"
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


def logout_view(request):
    logout(request)
    return redirect('accounts:login')