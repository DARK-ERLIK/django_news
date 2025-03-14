from django.db import models
from django.contrib.auth.models import User


class NewsCategory(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name="Категория")

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержание")
    category = models.ForeignKey(NewsCategory, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(upload_to='news_images/', null=True, blank=True, verbose_name="Изображение")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")

    def __str__(self):
        return self.title


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    favorite_news = models.ManyToManyField(News, related_name="favorited_by", blank=True)

    def __str__(self):
        return f'Профиль пользователя {self.user.username}'


class FavoriteNews(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="favorite_news")
    news = models.ForeignKey(News, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'news')

    def __str__(self):
        return f"{self.user.username} добавил в избранное: {self.news.title}"
