from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import News, FavoriteNews

def home(request):
    news_list = News.objects.all()
    return render(request, 'news/home.html', {'news_list': news_list})

def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
    return render(request, "news/login.html")

def user_logout(request):
    logout(request)
    return redirect("home")

@login_required
def add_to_favorites(request, news_id):
    news_item = News.objects.get(id=news_id)
    FavoriteNews.objects.get_or_create(user=request.user, news=news_item)
    return redirect("home")

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "news/register.html", {"form": form})

