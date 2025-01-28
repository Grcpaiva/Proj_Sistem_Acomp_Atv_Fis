from django.shortcuts import render
from django.views import View
from .models import PessoaFisica, PessoaJuridica, Academia, Modalidade, Exercicio, Frequencia, Cidade, PlanoDeTreino, Ocorrencia

class IndexView(View):
    def get(self, request):
        pessoas_fisicas = PessoaFisica.objects.all()
        pessoas_juridicas = PessoaJuridica.objects.all()
        academias = Academia.objects.all()  
        modalidades = Modalidade.objects.all()
        exercicios = Exercicio.objects.all()
        frequencias = Frequencia.objects.all()
        cidades = Cidade.objects.all()
        planos_de_treino = PlanoDeTreino.objects.all()
        ocorrencias = Ocorrencia.objects.all()

        return render(request, 'index.html', {
            'pessoas_fisicas': pessoas_fisicas,
            'pessoas_juridicas': pessoas_juridicas,
            'academias': academias, 
            'modalidades': modalidades,
            'exercicios': exercicios,
            'frequencias': frequencias,
            'cidades': cidades,
            'planos_de_treino': planos_de_treino,
            'ocorrencias': ocorrencias,
        })
