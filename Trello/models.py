from django.db import models
from django.contrib.auth.models import User

class Projeto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projetos')
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome


class Tarefa(models.Model):
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('andamento', 'Em andamento'),
        ('concluida', 'Concluída'),
    ]

    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE, related_name='tarefas')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pendente')
    prazo = models.DateField(null=True, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo