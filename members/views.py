from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from .forms import RegisterUserForm, PasswordChangingForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy

def login_user(request):
    if request.method== "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You are logged in!")
            return redirect('info')
        else:
            messages.success(request, "There was an error loging in, please try again...")
            return redirect('login')

    else:
        return render(request, 'authenticate/login.html',{
            })

def logout_user(request):
    logout(request)
    messages.success(request, "You are logged out!")
    return redirect('login')

def register_user(request):
    if request.method== "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Registration successful! Welcome")
            return redirect('info')

    else:
        form = RegisterUserForm()
    return render(request, 'authenticate/register_user.html', {
            'form' : form
        })


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy('login')