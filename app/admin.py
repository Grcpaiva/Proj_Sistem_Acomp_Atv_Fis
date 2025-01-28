from django.contrib import admin
from .models import Academia, PessoaFisica, PessoaJuridica, Modalidade, Exercicio, Frequencia, PlanoDeTreino, AvaliacaoFisica, Ocorrencia, TipoAvaliacao, Cidade, UF

class AcademiaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'cnpj', 'endereco', 'telefone', 'cidade']
    search_fields = ['nome', 'cnpj', 'endereco']
    list_filter = ['cidade']

admin.site.register(Academia, AcademiaAdmin)

class PessoaJuridicaAdmin(admin.ModelAdmin):
    list_display = ['razao_social', 'cnpj', 'academia', 'cidade']
    search_fields = ['razao_social', 'cnpj']
    list_filter = ['cidade', 'academia']

admin.site.register(PessoaJuridica, PessoaJuridicaAdmin)

class PessoaFisicaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'cpf', 'data_nasc', 'cidade']
    search_fields = ['nome', 'cpf']
    list_filter = ['cidade']

admin.site.register(PessoaFisica, PessoaFisicaAdmin)

class ModalidadeAdmin(admin.ModelAdmin):
    list_display = ['nome']
    search_fields = ['nome']

admin.site.register(Modalidade, ModalidadeAdmin)

class ExercicioAdmin(admin.ModelAdmin):
    list_display = ['nome', 'modalidade']
    search_fields = ['nome', 'modalidade__nome']
    list_filter = ['modalidade']

admin.site.register(Exercicio, ExercicioAdmin)

class PlanoDeTreinoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'academia', 'pessoa']
    search_fields = ['nome', 'academia__razao_social', 'pessoa__nome']
    list_filter = ['academia']

admin.site.register(PlanoDeTreino, PlanoDeTreinoAdmin)

class AvaliacaoFisicaAdmin(admin.ModelAdmin):
    list_display = ['descricao', 'plano_de_treino', 'tipo_avaliacao', 'nota']
    search_fields = ['descricao', 'plano_de_treino__nome', 'tipo_avaliacao__nome']
    list_filter = ['tipo_avaliacao']

admin.site.register(AvaliacaoFisica, AvaliacaoFisicaAdmin)

class FrequenciaAdmin(admin.ModelAdmin):
    list_display = ['plano_de_treino', 'exercicio', 'pessoa', 'numero_faltas']
    search_fields = ['pessoa__nome', 'plano_de_treino__nome', 'exercicio__nome']
    list_filter = ['plano_de_treino']

admin.site.register(Frequencia, FrequenciaAdmin)

class OcorrenciaAdmin(admin.ModelAdmin):
    list_display = ['descricao', 'data', 'plano_de_treino', 'exercicio', 'pessoa']
    search_fields = ['descricao', 'plano_de_treino__nome', 'exercicio__nome', 'pessoa__nome']
    list_filter = ['plano_de_treino', 'exercicio']

admin.site.register(Ocorrencia, OcorrenciaAdmin)

class TipoAvaliacaoAdmin(admin.ModelAdmin):
    list_display = ['nome']
    search_fields = ['nome']

admin.site.register(TipoAvaliacao, TipoAvaliacaoAdmin)

class CidadeAdmin(admin.ModelAdmin):
    list_display = ['nome', 'uf']
    search_fields = ['nome']
    list_filter = ['uf']

admin.site.register(Cidade, CidadeAdmin)

class UFAdmin(admin.ModelAdmin):
    list_display = ['sigla']
    search_fields = ['sigla']

admin.site.register(UF, UFAdmin)
