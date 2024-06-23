from django.urls import path
from . import views

app_name = 'login'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'), # Adicione esta linha
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
]

