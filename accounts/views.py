from django.shortcuts import render, redirect
from .forms import Register_form,Login_form
from django.contrib import messages
from django.contrib.auth import login, logout

def register(request):
    if request.method == "POST":
        form = Register_form(request.POST)

        if form.is_valid():
            user = form.save()
            messages.success(request, "Registro completado correctamente.")
            return redirect('index')
    else:
        form = Register_form()
        
    return render(request, 'accounts/register.html', {'form' : form})

def login(request):
    login_form = Login_form
    return render(request, 'accounts/login.html', {'form': login_form})