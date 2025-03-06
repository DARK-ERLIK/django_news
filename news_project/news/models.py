from django.db import models
from django.contrib.auth.models import User
import os

# Create your models here.
class NewsCategory(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название категории")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")

    def __str__(self):
        return self.name

class News(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Основной текст")
    category = models.ForeignKey(NewsCategory, on_delete=models.CASCADE, verbose_name="Категория")
    image = models.ImageField(upload_to='news_images/', null=True, blank=True, verbose_name="Изображение")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")

    def __str__(self):
        return self.title

class FavoriteNews(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    news = models.ForeignKey(News, on_delete=models.CASCADE)
