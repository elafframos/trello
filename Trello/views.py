from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Projeto, Tarefa
from django.db.models import Q


# Cadastro de usuário
def cadastro_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            User.objects.create_user(username=username, email=email, password=password)
            return redirect('login_view')  # após cadastro, vai para login
        else:
            return render(request, 'cadastro.html', {'erro': 'Usuário já existe!'})
    return render(request, 'cadastro.html')

# Login do usuário
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('tarefa_view')  # após login, vai para a lista de tarefas
        else:
            return render(request, 'login.html', {'erro': 'Usuário ou senha inválidos'})
    return render(request, 'login.html')

# Logout do usuário
def logout_view(request):
    logout(request)
    return redirect('login_view')

# Página de tarefas (protegida)
@login_required(login_url='login_view')
def tarefa_view(request):
    termo = request.GET.get('search', '')  # pega o termo do input "search"
    
    if termo:
        projetos = Projeto.objects.filter(
            Q(nome__icontains=termo) | Q(descricao__icontains=termo),
            usuario=request.user
        ).prefetch_related('tarefas')
    else:
        projetos = Projeto.objects.filter(usuario=request.user).prefetch_related('tarefas')

    return render(request, 'index.html', {'projetos': projetos, 'termo': termo})

@login_required(login_url='login_view')
def adicionar_view(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        if nome:
            Projeto.objects.create(nome=nome, descricao=descricao, usuario=request.user)
            return redirect('tarefa_view')
    return render(request, 'adicionar_projeto.html')

from django.shortcuts import get_object_or_404

@login_required(login_url='login_view')
def editar_view(request, projeto_id):
    projeto = get_object_or_404(Projeto, id=projeto_id, usuario=request.user)

    if request.method == 'POST':
        projeto.nome = request.POST.get('nome')
        projeto.descricao = request.POST.get('descricao')
        projeto.save()
        return redirect('tarefa_view')

    return render(request, 'editar_projeto.html', {'projeto': projeto})

@login_required(login_url='login_view')
def remover_view(request, projeto_id):
    projeto = get_object_or_404(Projeto, id=projeto_id, usuario=request.user)

    if request.method == 'POST':
        projeto.delete()
        return redirect('tarefa_view')

    return render(request, 'confirmar_remocao.html', {'projeto': projeto})

@login_required(login_url='login_view')
def adicionar_tarefa(request, projeto_id):
    projeto = get_object_or_404(Projeto, id=projeto_id, usuario=request.user)

    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        status = request.POST.get('status')
        if titulo:
            Tarefa.objects.create(
                titulo=titulo,
                descricao=descricao,
                status=status,
                projeto=projeto
            )
            return redirect('tarefa_view')
    return render(request, 'adicionar_tarefa.html', {'projeto': projeto})