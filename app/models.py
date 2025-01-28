from django.db import models

class UF(models.Model):
    sigla = models.CharField(max_length=2)

    def __str__(self):
        return self.sigla

class Cidade(models.Model):
    nome = models.CharField(max_length=100)
    uf = models.ForeignKey(UF, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nome

class Academia(models.Model):
    nome = models.CharField(max_length=255)  
    cnpj = models.CharField(max_length=14, unique=True)  
    razao_social = models.CharField(max_length=255, blank=True, null=True)  
    endereco = models.CharField(max_length=255, blank=True, null=True) 
    telefone = models.CharField(max_length=15, blank=True, null=True)  
    cidade = models.ForeignKey(Cidade, on_delete=models.SET_NULL, null=True, blank=True)  

    def __str__(self):
        return self.nome

class Pessoa(models.Model):
    nome = models.CharField(max_length=255)
    nome_do_pai = models.CharField(max_length=255, blank=True, null=True)
    nome_da_mae = models.CharField(max_length=255, blank=True, null=True)
    cpf = models.CharField(max_length=11, unique=True)
    data_nasc = models.DateField()
    email = models.EmailField(max_length=255)
    cidade = models.ForeignKey(Cidade, on_delete=models.SET_NULL, null=True, blank=True)
    ocupacao = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.nome

class PessoaFisica(Pessoa):
    class Meta:
        verbose_name = 'Pessoa Física'
        verbose_name_plural = 'Pessoas Físicas'

class PessoaJuridica(Pessoa):
    academia = models.ForeignKey(Academia, on_delete=models.SET_NULL, null=True, blank=True)  
    razao_social = models.CharField(max_length=255, blank=True, null=True)
    cnpj = models.CharField(max_length=14, unique=True)

    class Meta:
        verbose_name = 'Pessoa Jurídica'
        verbose_name_plural = 'Pessoas Jurídicas'

class Modalidade(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class Exercicio(models.Model):
    nome = models.CharField(max_length=255)
    modalidade = models.ForeignKey(Modalidade, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class PlanoDeTreino(models.Model):
    nome = models.CharField(max_length=255)
    academia = models.ForeignKey(Academia, on_delete=models.SET_NULL, null=True, blank=True)
    pessoa = models.ForeignKey(PessoaFisica, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nome

class TipoAvaliacao(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class AvaliacaoFisica(models.Model):
    descricao = models.TextField()
    plano_de_treino = models.ForeignKey(PlanoDeTreino, on_delete=models.SET_NULL, null=True, blank=True)
    tipo_avaliacao = models.ForeignKey(TipoAvaliacao, on_delete=models.SET_NULL, null=True, blank=True)
    nota = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f'Avaliação: {self.descricao}'

class Frequencia(models.Model):
    plano_de_treino = models.ForeignKey(PlanoDeTreino, on_delete=models.SET_NULL, null=True, blank=True)
    exercicio = models.ForeignKey(Exercicio, on_delete=models.SET_NULL, null=True, blank=True)
    pessoa = models.ForeignKey(PessoaFisica, on_delete=models.SET_NULL, null=True, blank=True)
    numero_faltas = models.IntegerField()

    def __str__(self):
        return f'{self.pessoa.nome if self.pessoa else "Pessoa não definida"} - Faltas: {self.numero_faltas}'

class Ocorrencia(models.Model):
    descricao = models.TextField()
    data = models.DateField()
    plano_de_treino = models.ForeignKey(PlanoDeTreino, on_delete=models.SET_NULL, null=True, blank=True)
    exercicio = models.ForeignKey(Exercicio, on_delete=models.SET_NULL, null=True, blank=True)
    pessoa = models.ForeignKey(PessoaFisica, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'Ocorrência em {self.data}: {self.descricao}'
