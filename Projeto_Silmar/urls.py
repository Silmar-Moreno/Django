from django.contrib import admin
from django.urls import path, include  # Importe include
from login import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('login.urls', namespace='login')),
    path('', views.index, name='index'),  # Adicione esta linha
]

