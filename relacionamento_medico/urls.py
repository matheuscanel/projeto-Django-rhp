from app import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.cadastro, name = 'cadastro' ),
    path('cadastro/', views.cadastro, name = 'cadastro' ),
    path('cadastro/concluido', views.cadastro_concluido, name = 'cadastro_concluido')
]
