from django.contrib import admin

# Register your models here.
from blog.models import Post
from blog.models import Professor
from blog.models import Coordenaçao
from blog.models import Funcionario
from blog.models import Matricula
from blog.models import Curso
from blog.models import Aluno
from blog.models import Turma
from blog.models import Evento
from blog.models import Biblioteca
from blog.models import Calendario
from blog.models import Duvida
from blog.models import Lanche
from blog.models import Cantina
from blog.models import Comentario

admin.site.register(Post)
admin.site.register(Professor)
admin.site.register(Coordenaçao)
admin.site.register(Funcionario)
admin.site.register(Matricula)
admin.site.register(Curso)
admin.site.register(Aluno)
admin.site.register(Turma)
admin.site.register(Evento)
admin.site.register(Biblioteca)
admin.site.register(Calendario)
admin.site.register(Duvida)
admin.site.register(Lanche)
admin.site.register(Cantina)
admin.site.register(Comentario)