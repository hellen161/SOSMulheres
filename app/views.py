from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import AlertaRapido, Denuncia, RedeApoio, Informacao, AvaliacaoRisco
from .forms import (
    AlertaRapidoForm, DenunciaForm, RedeApoioForm, InformacaoForm, AvaliacaoRiscoForm
)

# ========== LISTAGEM ==========

def home(request):
    return render(request, 'home.html')


def alerta_rapido_list(request):
    if not request.user.is_authenticated or not request.user.is_staff:
        return redirect('home')
    alertas = AlertaRapido.objects.all()
    return render(request, 'alerta_rapido_list.html', {'alertas': alertas})


def denuncia_list(request):
    if not request.user.is_authenticated or not request.user.is_staff:
        return redirect('home')
    denuncias = Denuncia.objects.all()
    return render(request, 'denuncia_list.html', {'denuncias': denuncias})


def rede_apoio_list(request):
    if not request.user.is_authenticated or not request.user.is_staff:
        return redirect('home')
    redes = RedeApoio.objects.all()
    return render(request, 'rede_apoio_list.html', {'redes': redes})


def informacao_list(request):
    if not request.user.is_authenticated or not request.user.is_staff:
        return redirect('home')
    informacoes = Informacao.objects.all()
    return render(request, 'informacao_list.html', {'informacoes': informacoes})


def avaliacao_risco_list(request):
    if not request.user.is_authenticated or not request.user.is_staff:
        return redirect('home')
    avaliacoes = AvaliacaoRisco.objects.all()
    return render(request, 'avaliacao_risco_list.html', {'avaliacoes': avaliacoes})


# ========== CADASTRO (CREATE) ==========

def alerta_rapido_create(request):
    if request.method == 'POST':
        form = AlertaRapidoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Alerta cadastrado com sucesso!')
            return redirect('alerta_rapido_list')
        else:
            messages.error(request, 'Por favor, corrija os erros abaixo.')
    else:
        form = AlertaRapidoForm()

    context = {
        'form': form,
        'titulo_formulario': 'Cadastro de Alerta Rápido'
    }
    return render(request, 'form.html', context)


def denuncia_create(request):
    if request.method == 'POST':
        form = DenunciaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Denúncia cadastrada com sucesso!')
            return redirect('denuncia_list')
        else:
            messages.error(request, 'Por favor, corrija os erros abaixo.')
    else:
        form = DenunciaForm()

    context = {
        'form': form,
        'titulo_formulario': 'Cadastro de Denúncia'
    }
    return render(request, 'form.html', context)


def rede_apoio_create(request):
    if request.method == 'POST':
        form = RedeApoioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Rede de Apoio cadastrada com sucesso!')
            return redirect('rede_apoio_list')
        else:
            messages.error(request, 'Por favor, corrija os erros abaixo.')
    else:
        form = RedeApoioForm()

    context = {
        'form': form,
        'titulo_formulario': 'Cadastro de Rede de Apoio'
    }
    return render(request, 'form.html', context)


def informacao_create(request):
    if request.method == 'POST':
        form = InformacaoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Informação cadastrada com sucesso!')
            return redirect('informacao_list')
        else:
            messages.error(request, 'Por favor, corrija os erros abaixo.')
    else:
        form = InformacaoForm()

    context = {
        'form': form,
        'titulo_formulario': 'Cadastro de Informação'
    }
    return render(request, 'form.html', context)


def avaliacao_risco_create(request):
    if request.method == 'POST':
        form = AvaliacaoRiscoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Avaliação de Risco cadastrada com sucesso!')
            return redirect('avaliacao_risco_list')
        else:
            messages.error(request, 'Por favor, corrija os erros abaixo.')
    else:
        form = AvaliacaoRiscoForm()

    context = {
        'form': form,
        'titulo_formulario': 'Cadastro de Avaliação de Risco'
    }
    return render(request, 'form.html', context)


class DenunciaCreateView(CreateView):
    def form_valid(self, form):
        send_mail('Nova denúncia enviada', f'''Uma nova denúncia foi registrada no sistema. Verifique o painel de administração.''', 'elizluzamor@gmail.com', ['elizluzamor@gmail.com'])
        return super().form_valid(form)


class AlertaRapidoCreateView(CreateView):
    def form_valid(self, form):
        send_mail('⚠️ Alerta Rápido acionado', f'''Alerta Rápido recebido! Verifique imediatamente o sistema SOSMulheres.''', 'elizluzamor@gmail.com', ['elizluzamor@gmail.com'])
        return super().form_valid(form)


class AvaliacaoRiscoCreateView(CreateView):
    def form_valid(self, form):
        send_mail('Nova Avaliação de Risco', f'''Uma nova Avaliação de Risco foi enviada por um usuário.''', 'elizluzamor@gmail.com', ['elizluzamor@gmail.com'])
        return super().form_valid(form)
