from django.urls import path
from .views import home, user_login, user_logout, add_to_favorites, register

urlpatterns = [
    path('', home, name='home'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('favorite/<int:news_id>/', add_to_favorites, name='add_to_favorites'),
    path('register/', register, name='register'),
]
