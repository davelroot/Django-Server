import uuid
from django.db import models
from django.urls import reverse
# Create your models here.


class Formadorcurso(models.Model):
   
    formador_id = models.AutoField(
		primary_key=True
	)
    name = models.CharField(
        max_length=250,
		blank=True,
		unique=True,
  )
    def __repr__(self):
        return '<Formadorcurso %r>' % self.name

class Periodocourso(models.Model):
  
    periodo_id = models.AutoField(
		primary_key=True
	)
    
    name = models.CharField(
        max_length=250,
		blank=True,
		unique=True,
  )
    def __repr__(self):
        return '<Periodocourso %r>' % self.name





class CarteiraMotorista(models.Model):

    #cursos_id = models.AutoField(
	#	primary_key=True
	#)
    carta_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
        )

    carta_nome = models.CharField(
        max_length=250,
		blank=True,
		unique=True,
  )
    carta_comentarioscursos = models.CharField(
        max_length=250,
		blank=True,
		unique=True,
  )
    carta_categoria = models.CharField(
        max_length=250,
		blank=True,
		unique=True,
  )
    carta_duracaocursos = models.CharField(
        max_length=250,
		blank=True,
		unique=True,
  )
    carta_price = models.CharField(
        max_length=250,
		blank=True,
		unique=True,
  )

    periodos = models.ManyToManyField(Periodocourso)  

    image_curso = models.ImageField(upload_to="cartaPitolto/", blank=True)
    date_created = models.DateField()
    
    def __repr__(self):
        return '<CarteiraMotorista %r>' % self.carta_nome
    
    def get_absolute_url(self): # new
        return reverse("cartaPiloto", args=[str(self.carta_id)])
################################################################################################
#                                         #
#                MOSTRAR ITENS            #        MOSTRAR ITENS
#                                         #
#                                         #
################################################################################################
class Cursosguardar(models.Model):

    #cursos_id = models.AutoField(
	#	primary_key=True
	#)
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
        )

    nomecursos = models.CharField(
        max_length=250,
		blank=True,
		unique=True,
  )
    comentarioscursos = models.CharField(
        max_length=250,
		blank=True,
		unique=True,
  )
    descriptioncursos = models.CharField(
        max_length=250,
		blank=True,
		unique=True,
  )
    datainiciocursos = models.CharField(
        max_length=250,
		blank=True,
		unique=True,
  )
    datafimcursos = models.CharField(
        max_length=250,
		blank=True,
		unique=True,
  )
    duracaocursos = models.CharField(
        max_length=250,
		blank=True,
		unique=True,
  )
    price = models.CharField(
        max_length=250,
		blank=True,
		unique=True,
  )

    periodos = models.ManyToManyField(Periodocourso)  
    licoes_1 = models.CharField(
        max_length=250,
		blank=True,
		unique=True,
  )
    licoes_2 = models.CharField(
        max_length=250,
		blank=True,
		unique=True,
  )
    licoes_3 = models.CharField(
        max_length=250,
		blank=True,
		unique=True,
  )
    licoes_4 = models.CharField(
        max_length=250,
		blank=True,
		unique=True,
  )
    licoes_5 = models.CharField(
        max_length=250,
		blank=True,
		unique=True,
  )

    image_curso  = models.ImageField(upload_to="cursosProfissionais/", blank=True)
    date_created = models.DateField()
    
    def __repr__(self):
        return '<Cursosguardar %r>' % self.name
    
    def get_absolute_url(self): # new
        return reverse("curso_detail", args=[str(self.id)])


class Alunosinscrito(models.Model):
    
    aluno_id= models.AutoField(
		primary_key=True
	)
    aluno_nome = models.CharField(
        max_length=250,
		blank=True,
		unique=True,
  )
    aluno_email = models.CharField(
        max_length=250,
		blank=True,
		unique=True,
  )
    aluno_contactos = models.CharField(
        max_length=250,
		blank=True,
		unique=True,
  )
    aluno_cursosfree = models.CharField(
        max_length=250,
		blank=True,
		unique=True,
  )
 
    aluno_bilhetebis = models.CharField(
        max_length=250,
		blank=True,
		unique=True,
  )
    alunoprecocursos = models.CharField(
        max_length=250,
		blank=True,
		unique=True,
  )
    aluno_duracaocursos = models.CharField(
        max_length=250,
		blank=True,
		unique=True,
  )
    periodo_id = models.CharField(
        max_length=250,
		blank=True,
		unique=True,
  )

    aluno_cursos = models.ManyToManyField(Cursosguardar)
     
    def __repr__(self):
        return '<Alunosinscrito %r>' % self.aluno_nome


class Evento_School(models.Model):
   
    eventos_id = models.AutoField(
		primary_key=True
	)
    event_name= models.CharField(
        max_length=250,
		blank=True,
		unique=True,
  )
    event_detalhes= models.CharField(
        max_length=250,
		blank=True,
		unique=True,
  )
    event_price= models.CharField(
        max_length=250,
		blank=True,
		unique=True,
  )
    event_data_inicio = models.CharField(
        max_length=250,
		blank=True,
		unique=True,
  )
    event_data_fim = models.CharField(
        max_length=250,
		blank=True,
		unique=True,
  )
    event_hora = models.CharField(
        max_length=250,
		blank=True,
		unique=True,
  )
    event_para_todos1 = models.CharField(
        max_length=250,
		blank=True,
		unique=True,
  )
    event_para_todos2 = models.CharField(
        max_length=250,
		blank=True,
		unique=True,
  )
    event_para_todos3= models.CharField(
        max_length=250,
		blank=True,
		unique=True,
  )
    event_theme1 = models.CharField(
        max_length=250,
		blank=True,
		unique=True,
  )
    event_theme2= models.CharField(
        max_length=250,
		blank=True,
		unique=True,
  )
    event_theme3 = models.CharField(
        max_length=250,
		blank=True,
		unique=True,
  )
    event_theme4 = models.CharField(
        max_length=250,
		blank=True,
		unique=True,
  )
    event_formadores = models.CharField(
        max_length=250,
		blank=True,
		unique=True,
  )
    event_periodos = models.CharField(
        max_length=250,
		blank=True,
		unique=True,
  )

    def __repr__(self):
        return '<Evento_School %r>' % self.name