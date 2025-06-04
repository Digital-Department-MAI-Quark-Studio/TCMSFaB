from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('article/create/', views.create_article, name='create_article'),
    path('article/<int:pk>/', views.view_article, name='view_article'),
    path('article/<int:pk>/edit/', views.edit_article, name='edit_article'),
    path('article/<int:pk>/delete/', views.delete_article, name='delete_article'),
    path('article/<int:pk>/like/', views.like_article, name='like_article'),
]