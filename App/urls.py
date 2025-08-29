"""
URL configuration for App project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Trello.views import login_view, tarefa_view, cadastro_view, logout_view, adicionar_view, editar_view, remover_view, adicionar_tarefa

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_view, name='login_view'),
    path('tarefa/', tarefa_view, name='tarefa_view'),
    path('cadastro/', cadastro_view, name='cadastro_view'),
    path('logout/', logout_view, name='logout_view'),
    path('adicionar/', adicionar_view, name='adicionar_view'),
    path('editar/<int:projeto_id>//', editar_view, name='editar_view'),
    path('excluir/editar/<int:projeto_id>//', remover_view, name='remover_view'),
    path('projeto/<int:projeto_id>/nova_tarefa/', adicionar_tarefa, name='adicionar_tarefa'),
]