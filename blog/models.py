from django.db import models
from django.contrib.auth.models import User

# Classe com as informações necessárias para que os alunos acessem suas contas
class Aluno(models.Model):
    nome = models.CharField(max_length=255, blank=False, null=False, verbose_name='Nome Completo')
    cpf = models.CharField(max_length=11, blank=False, null=False, verbose_name='CPF')
    email_aluno = models.EmailField(blank=True, null=True)

    def __str__(self):
        return str(self.nome)

# Classe com as informações necessárias para os professores acessarem suas contas
class Professor(models.Model):
    nome = models.CharField(max_length=255, blank=False, null=False, verbose_name='Nome Completo')
    email = models.EmailField(blank=True, null=True, verbose_name='E-mail')
    senha = models.CharField(max_length=16, blank=False, null=False)

    def __str__(self):
        return str(self.nome)

# Classe com as informações necessárias para os membros da coordenação acessarem suas contas
class Coordenaçao(models.Model):
    nome = models.CharField(max_length=255, blank=False, null=False, verbose_name='Nome Completo')
    email = models.EmailField(blank=True, null=True, verbose_name='E-mail')
    senha = models.CharField(max_length=16, blank=False, null=False)

    def __str__(self):
         return str(self.nome)

# Classe com as informações necessárias para os funcionários acessarem suas contas
class Funcionario(models.Model):
    nome = models.CharField(max_length=255, blank=False, null=False, verbose_name='Nome Completo')
    email = models.EmailField(blank=True, null=True, verbose_name='E-mail')
    senha = models.CharField(max_length=16, blank=False, null=False)

    def __str__(self):
        return str(self.nome)

# Classe dedicada a apresentar as informações necessárias para realização de matrícula
class Matricula(models.Model):
    nome = models.CharField(max_length=255, blank=False, null=False, verbose_name='Nome do Aluno')
    Sobrenome = models.CharField(max_length=255, blank=False, null=False, verbose_name='Sobrenome')
    Idade = models.DecimalField(max_digits=2, decimal_places=2, blank=False, null=False, verbose_name='Idade')
    email_aluno = models.EmailField(blank=True, null=True)
    senha = models.CharField(max_length=16, blank=False, null=False)
    confirmar_senha = models.CharField(max_length=16, blank=False, null=False)
    cpf = models.CharField(max_length=11, blank=False, null=False, verbose_name='CPF')
    conclusao_em = models.DateField(blank=False, null=False, verbose_name='Data de Conclusão do Ensino Médio')
    curso = models.ManyToManyField('Curso')
    valor_mensalidade = models.DecimalField(max_digits=6, decimal_places=2, blank=False, null=False)

    def __str__(self):
        return str(self.nome)

# Classe com as informações de cada Curso
class Curso(models.Model):
    nome = models.CharField(max_length=255, blank=False, null=False, verbose_name='Nome do Curso')
    data_inicio = models.DateField(blank=False, null=False, verbose_name='Data de Início do Semestre')
    data_conclusao = models.DateField(blank=False, null=False, verbose_name='Data de Conclusão do Curso')
    grade_curricular = models.TextField(blank=True, null=True, verbose_name='Grade Curricular')
    valor = models.DecimalField(max_digits=6, decimal_places=2, blank=False, null=False, verbose_name='Mensalidade')
    nome_aluno = models.ForeignKey('Aluno', on_delete=models.DO_NOTHING, default=1, verbose_name='Nome do Aluno')
    email_aluno = models.EmailField(blank=True, null=True)

    def __str__(self):
        return str(self.nome)

# Classe com as informações das Turmas de cada curso
class Turma(models.Model):
    nome_do_curso = models.ManyToManyField('Curso')
    semestre = models.DateField(blank=False, null=False, verbose_name='Semestre')
    qtd_alunos = models.DecimalField(max_digits=2, decimal_places=2, blank=False, null=False,
                                     verbose_name='Quantidade de Alunos')
    vagas_totais = models.DecimalField(max_digits=2, decimal_places=2, blank=False, null=False,
                                       verbose_name='Total de Vagas' )
    vagas_remanescentes = models.DecimalField(max_digits=2, decimal_places=2, blank=False, null=False,
                                              verbose_name='Vagas Remanescentes')
    data_de_inicio = models.DateField(blank=False, null=False, verbose_name='Data de Início do Curso')
    data_de_conclusao= models.DateField(blank=False, null=False, verbose_name='Data de Conclusão de Curso')

    def __str__(self):
        return str(self.nome_do_curso)

# Classe dedicada a abordar as informações dos eventos acadêmicos
class Evento(models.Model):
    nome_do_evento = models.CharField(max_length=255, blank=False, null=False, verbose_name='Nome do Evento')
    data = models.DateField(blank=False, null=False, verbose_name='Data do Evento')
    hora = models.TimeField(blank=False, null=False, verbose_name='Hora do Evento')
    data_e_hora = models.DateTimeField(blank=False, null=False, verbose_name='Data e Hora do Evento')
    resumo = models.CharField(max_length=255, blank=False, null=False, verbose_name='Resumo do Evento')
    observacao = models.TextField(blank=False, null=False, verbose_name='Observações sobre o Evento')
    palestrante = models.CharField(max_length=255, blank=False, null=False, verbose_name='Nome do Palestrante')
    email_palestrante = models.EmailField(blank=True, null=True)
    cursos_obrigatorios = models.CharField(max_length=255, blank=False, null=False)
    cursos_opcionais = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):
        return str(self.nome_do_evento)

# Classe com as informações sobre a biblioteca
class Biblioteca(models.Model):
    nome_livro = models.CharField(max_length=255, blank=False, null=False, verbose_name='Nome do Livro')
    data_publicacao = models.DateField(blank=False, null=False, verbose_name='Data de Publicação')
    autor_livro = models.CharField(max_length=255, blank=False, null=False, verbose_name='Autor do Livro')
    resumo_livro = models.TextField(max_length=255, blank=False, null=False)
    editora = models.CharField(max_length=255, blank=False, null=False, verbose_name='Editora')

    def __str__(self):
        return str(self.nome_livro)

# Classe com as datas de provas dos cursos
class Calendario(models.Model):
    nome_curso = models.ManyToManyField('Curso')
    data_p1 = models.DateField(blank=False, null=False, verbose_name='Data da prova 1')
    hora_p1 = models.TimeField(blank=False, null=False, verbose_name='Hora da Prova 1')
    data_p2 = models.DateField(blank=False, null=False, verbose_name='Data da Prova 2')
    hora_p2 = models.TimeField(blank=False, null=False, verbose_name='Hora da Prova 2')

    def __str__(self):
        return str(self.nome_curso)

# Classe dedicada a postagem de dúvidas
class Duvida(models.Model):
    seu_nome = models.CharField(max_length=255, blank=False, null=False, verbose_name='Seu Nome')
    seu_email = models.EmailField(blank=True, null=True)
    resumo_duvida = models.CharField(max_length=255, blank=False, null=False, verbose_name='Resumo da Dúvida')
    duvida = models.TextField(blank=False, null=False, verbose_name=('Escreva sua Dúvida'))
    data_hora = models.DateTimeField(auto_now_add=True, verbose_name=('Data e Hora da Dúvida'))

    def __str__(self):
        return str(self.seu_nome)

# Classe com as informações sobre lanches presentes na cantina
class Lanche(models.Model):
    nome_lanche = models.CharField(max_length=255, blank=False, null=False)
    ingredientes = models.TextField(blank=False, null=False)
    numero_produto = models.IntegerField(blank=False, null=False, default=0, verbose_name='Numero do Produto')

    def __str__(self):
        return str(self.nome_lanche)

# Classe com as informções sobre a cantina
class Cantina(models.Model):
    nome = models.CharField(max_length=255,blank=False, null=False)
    lanche = models.ManyToManyField('Lanche')
    data_fabricacao = models.DateField(blank=False, null=False, verbose_name='Data de Fabricação')
    data_validade = models.DateField(blank=False, null=False, verbose_name='Data de Validade')
    observacao = models.TextField(max_length=255, blank=False, null=False)
    valor = models.DecimalField(max_digits=6, decimal_places=2, blank=False, null=False)
    qtd_itens = models.IntegerField(blank=True, null=False, default=0, verbose_name='Quantidade de Itens')

    def __str__(self):
        return self.lanche + ' R$ ' + str(self.valor)


# Classe para posts livres dentro do blog
class Post(models.Model):
    titulo = models.CharField(max_length=255)
    resumo = models.CharField(max_length=255)
    conteudo = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.PROTECT)
    criado_em = models.DateField(auto_now_add=True)
    email_autor = models.EmailField(blank=True, null=True)
    hora_post = models.TimeField(auto_now_add=True)

    def __str__(self):
        return str(self.titulo)

# Classe para adicionar comentários aos posts
class Comentario(models.Model):
    nome = models.CharField(max_length=255, blank=False, null=False)
    descricao = models.TextField(max_length=300)
    autor_post = models.CharField(max_length=255, blank=False, null=False)
    nome_post = models.ManyToManyField('Post')
    data_post = models.DateField(blank=False, null=False, verbose_name='Data de publicação do Post')
    hora_post = models.TimeField(auto_now_add=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return str(self.nome_post)
