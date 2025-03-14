from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import News, FavoriteNews, UserProfile


def home(request):
    news_list = News.objects.all().order_by('-created_at')
    return render(request, 'news/home.html', {'news_list': news_list})


def user_login(request):
    form = AuthenticationForm(data=request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect('news:home')

    return render(request, "news/login.html", {'form': form})


def user_logout(request):
    logout(request)
    return redirect('news:home')


@login_required
def user_profile(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    favorite_news = user_profile.favorite_news.all()

    return render(request, 'news/profile.html', {'favorite_news': favorite_news})


@login_required
def add_to_favorites(request, news_id):
    news_item = get_object_or_404(News, id=news_id)
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    if not user_profile.favorite_news.filter(id=news_id).exists():
        user_profile.favorite_news.add(news_item)

    return redirect('news:home')


def user_register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user)
            login(request, user)
            return redirect('news:profile')
    else:
        form = UserCreationForm()

    return render(request, "news/register.html", {'form': form})
