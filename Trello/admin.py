from .models import Projeto, Tarefa
from django.contrib.auth.models import User
from django.contrib import admin

class adminProjeto(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'usuario', 'criado_em')
    search_fields = ('nome', )

    def save_model(self, request, obj, form, change):
        if not obj.usuario:
            obj.usuario = request.user
        obj.save()

admin.site.register(Projeto, adminProjeto)

@admin.register(Tarefa)
class adminTarefa(admin.ModelAdmin):
    list_display = ('titulo', 'projeto', 'status', 'prazo', 'criado_em')
    search_fields = ('titulo', )