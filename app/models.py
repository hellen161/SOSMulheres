from django.db import models
from django.utils import timezone

class AlertaRapido(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    localizacao = models.CharField(max_length=150)
    data_criacao = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.nome


class Denuncia(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    localizacao = models.CharField(max_length=150)
    data_criacao = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.nome


class RedeApoio(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=150)
    telefone = models.CharField(max_length=20)
    descricao = models.TextField()
    data_criacao = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.nome


class Informacao(models.Model):
    titulo = models.CharField(max_length=150)
    descricao = models.TextField()
    categoria = models.CharField(max_length=100)
    data_criacao = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.titulo


class AvaliacaoRisco(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    nivel_risco = models.CharField(
        max_length=50,
        choices=[
            ('baixo', 'Baixo'),
            ('moderado', 'Moderado'),
            ('alto', 'Alto'),
            ('critico', 'Crítico')
        ]
    )
    data_criacao = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return f"{self.nome} - {self.nivel_risco.capitalize()}"
