from django.shortcuts import render, redirect
from .forms import InfoForm
from .models import info, category_Class, category_edition, FilesUpload


# Create your views here.
def home(request):
    return render(request, "dndating/home.html",{})


def info_user(request):
    if request.method == "POST":
        form = InfoForm(request.POST, request.FILES)
        if form.is_valid():
            form_new_listing = form.save(commit=False)
            form_new_listing.user = request.user
            form_new_listing.save()
            # Redirect user to index
            return redirect('index')
    else:
        form = InfoForm
        return render(request, "dndating/info.html",{
            "form" : form
        })


def index(request):
    user = request.user
    active_user = info.objects.filter(IsActive=True)
    return render(request, "dndating/active_users.html", {
    "active_user" : active_user,
    "user" : user
    })


def edit_info(request, info_id):
    info_user = info.objects.get(pk=info_id)
    form = InfoForm(request.POST or None, request.FILES or None, instance=info_user)
    if form.is_valid():
        form.save()
        # Redirect user to index
        return redirect('index')
    return render(request, 'dndating/edit.html',{
        'user' : info_user,
        'form' : form
    })


def show_profile(request, info_id):
    info_user = info.objects.get(pk=info_id)
    return render(request, "dndating/show_profile.html",{
        'info' : info_user

    })


def close_profile(request, info_id):
    info_user = info.objects.get(pk=info_id)
    info_user.IsActive = False
    info_user.save()
    return render(request, "authenticate/login.html", {
        'update' : True,
        'user' : info_user,
    })


def search_players(request):
    if request.method == "POST":
        searched = request.POST['searched']#if doesnt work try ('searched')
        players = info.objects.filter(name__contains = searched, IsActive=True)
        return render(request, "dndating/search_players.html", {
            'searched' : searched,
            'players' : players,
        })
    else:
        return render(request, "dndating/search_players.html", {
        })

