from django.shortcuts import render
from .models import News

def home(request):
    news_list = News.objects.all()
    return render(request, 'news/home.html', {'news_list': news_list})
