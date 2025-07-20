from django import forms
from .models import AlertaRapido, Denuncia, RedeApoio, Informacao, AvaliacaoRisco


class AlertaRapidoForm(forms.ModelForm):
    class Meta:
        model = AlertaRapido
        fields = ['nome', 'descricao', 'localizacao']
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 4}),
        }


class DenunciaForm(forms.ModelForm):
    class Meta:
        model = Denuncia
        fields = ['nome', 'descricao', 'localizacao']
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 4}),
        }


class RedeApoioForm(forms.ModelForm):
    class Meta:
        model = RedeApoio
        fields = ['nome', 'endereco', 'telefone', 'descricao']
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 3}),
        }


class InformacaoForm(forms.ModelForm):
    class Meta:
        model = Informacao
        fields = ['titulo', 'descricao', 'categoria']
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 4}),
        }


class AvaliacaoRiscoForm(forms.ModelForm):
    class Meta:
        model = AvaliacaoRisco
        fields = ['nome', 'descricao', 'nivel_risco']
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 4}),
        }
