from django.db import models



class Logotiposglass(models.Model):
    id = models.AutoField(
		primary_key=True
	)
    nametitle = models.CharField(
        max_length=250,
		blank=True,
		unique=True,
  )
    
    image_1logo = models.ImageField(
		upload_to='static/logotiposUpadate/',
		unique=True,

	)
    image_2logo = models.ImageField(
		upload_to='static/logotiposUpadate/',
		unique=True,

	)
    image_3logo = models.ImageField(
		upload_to='static/logotiposUpadate/',
		unique=True,

	)
    contactglass = models.CharField(
		'Telefone  1',
		max_length=12,
		blank=True,
		unique=True,		
	)
    contactglass2 = models.CharField(
		'Telefone 2',
		max_length=12,
		blank=True,
		unique=True,
	)
    contactglass3 = models.CharField(
		'Telefone 3',
		max_length=12,
		blank=True,
		unique=True,
	)
    emailsglass = models.EmailField(
		'Email',
		max_length=250,
		blank=True,
		null=True,
		unique=True,
		

	)
    emailsglass2 = models.EmailField(
		'Email 2',
		max_length=250,
		blank=True,
		null=True,
		unique=True,
		

	)
    emailsglass3 = models.EmailField(
		'Email 3',
		max_length=250,
		blank=True,
		null=True,
		unique=True,
		

	)
    descriptionsglass = models.TextField(
		'Descricao',
		max_length=900,
		blank=True,
		unique=True,
		
	)
    termosecondicoes = models.TextField(
		'Termos&Condicoes',
		max_length=900,
		blank=True,
		unique=True,
		
	)
    politicasglass = models.TextField(
		'Nossa Politica',
		max_length=900,
		blank=True,
		unique=True,
		
	)
    sobresglass = models.TextField(
		'Sobre Nos ',
		max_length=900,
		blank=True,
		unique=True,
		
	)
    quemesomosglass = models.TextField(
		'Quem Somos',
		max_length=990,
		blank=True,
		unique=True,
		
	)
    

# Create your models here.
#class Post(models.Model):
#    
#    post_id = models.AutoField(
#		primary_key=True
#	)
#    text = db.Column(db.Text, nullable=False)
#    date_created = db.Column(db.DateTime(timezone=True), nullable=False, default=datetime.utcnow)
#    author_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
#    comments = db.relationship('Comment', backref='post', passive_deletes=True)
#    likes = db.relationship('Like', backref='post', passive_deletes=True)
#    
#    def __repr__(self):
#        return f"Post('{self.text}', '{self.date_created}', '{self.comments}')"


#################################################
#
#
#
#
#################################################
#class Comment(models.Model):
 #  
 #   comment_id = models.AutoField(
#		primary_key=True
#	)
 #   text = db.Column(db.String(200), nullable=False)
 #   date_created = db.Column(db.DateTime(timezone=True), default=func.now())
 #   author = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
 #   post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
 #   
 #   def __repr__(self):
 #       return f"Comment('{self.text}', '{self.date_created}', '{self.author}')"
#################################################################################################
#                                         #
#                MOSTRAR ITENS            #        MOSTRAR ITENS
#                                         #
#                                         #
################################################################################################
#class Like(models.Model):
#  
#    link_id = models.AutoField(
#		primary_key=True
#	)
#    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
#    author = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
#    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
#
#    def __repr__(self):
#        return f"Like('{self.date_created}', '{self.author}')"
################################################################################################
#                                         #
#                Briefingwebsites            #        Briefingwebsites
#                                         #
#                                         #
################################################################################################

class Briefingwebsites(models.Model):

    sites_id = models.AutoField(
		primary_key=True
	)
    func_nameDaEmpresa = models.CharField(
        max_length=250,
		blank=True,
		unique=True,
  )
    
    func_localizacaoDaEmpresa = models.CharField(
        max_length=250,
		blank=True,
		unique=True,
  )
    
    func_EmailDaEmpresa =  models.CharField(
        max_length=250,
		blank=True,
		unique=True,
  )
    
    func_conctatoDaEmpresa = models.CharField(
        max_length=250,
		blank=True,
		unique=True,
  )
    
    func_sobreSuaEmpresa = models.CharField(
        max_length=250,
		blank=True,
		unique=True,
  )
    
    func_objetivoDoSeuSite= models.CharField(
        max_length=250,
		blank=True,
		unique=True,
  )
    
    func_sitesReferencia = models.CharField(
        max_length=250,
		blank=True,
		unique=True,
  )
    
    func_coresPadraoVcQuer= models.CharField(
        max_length=250,
		blank=True,
		unique=True,
  )
    
    func_plano_preco = models.CharField(
        max_length=250,
		blank=True,
		unique=True,
  )
    
    date_created = models.DateField(

  )
    

#    def __repr__(self):
#        return f"TypoBriefing('{self.func_nameDaEmpresa}',
#                       '{self.func_localizacaoDaEmpresa}',
#                       '{self.func_EmailDaEmpresa}',
#                       '{self.func_conctatoDaEmpresa}',
#                       '{self.func_sobreSuaEmpresa}',
#                       '{self.func_objetivoDoSeuSite}',
#                       '{self.func_sitesReferencia}',
#                       '{self.func_coresPadraoVcQuer}',
#                       '{self.func_plano_preco}',
#                       '{self.date_created}',
#                      )"


class Briefinglojavirtual(models.Model):
   
    virtual_id = models.AutoField(
		primary_key=True
	)
    loja_nameDaEmpresa = models.CharField(
        max_length=250,
		blank=True,
		unique=True,
  )
    
    loja_localizacaoDaEmpresa = models.CharField(
        max_length=250,
		blank=True,
		unique=True,
  )
    
    loja_EmailDaEmpresa = models.CharField(
        max_length=250,
		blank=True,
		unique=True,
  )
    
    loja_conctatoDaEmpresa = models.CharField(
        max_length=250,
		blank=True,
		unique=True,
  )
    
    loja_sobreSuaEmpresa = models.CharField(
        max_length=250,
		blank=True,
		unique=True,
  )
    
    loja_objetivoDoSeuSite= models.CharField(
        max_length=250,
		blank=True,
		unique=True,
  )
    
    loja_sitesReferencia = models.CharField(
        max_length=250,
		blank=True,
		unique=True,
  )
    
    loja_coresPadraoVcQuer = models.CharField(
        max_length=250,
		blank=True,
		unique=True,
  )
    
    loja_plano_preco= models.CharField(
        max_length=250,
		blank=True,
		unique=True,
  )
    
    date_created = models.DateField(

  )

#    def __repr__(self):
#        return f"TypoBriefing('{self.loja_nameDaEmpresa }',
#                       '{self.loja_localizacaoDaEmpresa}',
#                       '{self.loja_EmailDaEmpresa}',
#                       '{self.loja_conctatoDaEmpresa}',
#                       '{self.loja_sobreSuaEmpresa}',
#                       '{self.loja_objetivoDoSeuSite}',
#                       '{self.loja_sitesReferencia}',
#                       '{self.loja_coresPadraoVcQuer}',
#                       '{self.aplica_plano_preco}',
#                       '{self.date_created}',
#                      )"

class Briefingapplication(models.Model):
  
    aplication_id = models.AutoField(
		primary_key=True
	)
    aplica_nameDaEmpresa = models.CharField(
        max_length=250,
		blank=True,
		unique=True,
  )
    
    aplica_localizacaoDaEmpresa = models.CharField(
        max_length=250,
		blank=True,
		unique=True,
  )
    
    aplica_EmailDaEmpresa = models.CharField(
        max_length=250,
		blank=True,
		unique=True,
  )
    
    aplica_conctatoDaEmpresa = models.CharField(
        max_length=250,
		blank=True,
		unique=True,
  )
    
    aplica_objetosocial= models.CharField(
        max_length=250,
		blank=True,
		unique=True,
  )
    
    aplica_sobreSuaEmpresa = models.CharField(
        max_length=250,
		blank=True,
		unique=True,
  )
    
    aplica_plano_preco = models.CharField(
        max_length=250,
		blank=True,
		unique=True,
  )
    
    date_created = models.DateField(

  )
    

#    def __repr__(self):
#        return f"TypoBriefing('{self.aplica_nameDaEmpresa}',
#                       '{self.aplica_localizacaoDaEmpresa}',
#                       '{self.aplica_EmailDaEmpresa}',
#                       '{self.aplica_conctatoDaEmpresa}',
#                       '{self.aplica_objetosocial}',
#                       '{self.aplica_sobreSuaEmpresa}',
#                       '{self.aplica_categoriasDoSeuSite}',
#                       '{self.aplica_plano_preco}',
#                       '{self.date_created}',
#                      )"


class Briefinglogotipo(models.Model):

    logo_id = models.AutoField(
		primary_key=True
	)
    logo_nameDaEmpresa = models.CharField(
        max_length=250,
		blank=True,
		unique=True,
  )
    
    logo_localizacaoDaEmpresa = models.CharField(
        max_length=250,
		blank=True,
		unique=True,
  )
    
    logo_EmailDaEmpresa = models.EmailField(
		'Email',
		max_length=250,
		blank=True,
		null=True,
		unique=True,
		

	)
    logo_conctatoDaEmpresa = models.CharField(
        max_length=250,
		blank=True,
		unique=True,
  )
    
    logo_sugestaoDeDominio= models.CharField(
        max_length=250,
		blank=True,
		unique=True,
  )
    
    logo_sobreSuaEmpresa= models.CharField(
        max_length=250,
		blank=True,
		unique=True,
  )
    
    logo_objetivoDoSeuSite = models.CharField(
        max_length=250,
		blank=True,
		unique=True,
  )
    
    logo_venderProduto = models.CharField(
        max_length=250,
		blank=True,
		unique=True,
  )
    
    logo_categoriasDoSeuSite = models.CharField(
        max_length=250,
		blank=True,
		unique=True,
  )
    
    logo_sitesReferencia = models.CharField(
        max_length=250,
		blank=True,
		unique=True,
  )
    
    logo_coresPadraoVcQuer= models.CharField(
        max_length=250,
		blank=True,
		unique=True,
  )
    
    logo_coresVoceNaoQuer= models.CharField(
        max_length=250,
		blank=True,
		unique=True,
  )
    
    logo_funcionalidadeExtra = models.CharField(
        max_length=250,
		blank=True,
		unique=True,
  )
    
    logo_imgansFornecida  = models.ImageField(
		upload_to='static/logotiposUpadate/',
		unique=True,)
    
    logo_picture = models.ImageField(
		upload_to='static/logotiposUpadate/',
		unique=True,

	)
    logo_sobreseuwebsite  = models.ImageField(
		upload_to='static/logotiposUpadate/',
		unique=True,)
    
    date_created = models.DateField(

  )
    



class Briefinghospedagem(models.Model):
   
    hosp_id = models.AutoField(
		primary_key=True
	)
    hosp_nameDaEmpresa = models.CharField(
        max_length=250,
		blank=True,
		unique=True,
  )
    hosp_localizacaoDaEmpresa = models.CharField(
        max_length=250,
		blank=True,
		unique=True,
  )
    hosp_EmailDaEmpresa = models.CharField(
        max_length=250,
		blank=True,
		unique=True,
  )
    hosp_conctatoDaEmpresa = models.CharField(
        max_length=250,
		blank=True,
		unique=True,
  )
    hosp_sugestaoDeDominio= models.CharField(
        max_length=250,
		blank=True,
		unique=True,
  )
    hosp_sobreSuaEmpresa = models.CharField(
        max_length=250,
		blank=True,
		unique=True,
  )
    hosp_objetivoDoSeuSite = models.CharField(
        max_length=250,
		blank=True,
		unique=True,
  )
    hosp_venderProduto = models.CharField(
        max_length=250,
		blank=True,
		unique=True,
  )
    hosp_categoriasDoSeuSite = models.CharField(
        max_length=250,
		blank=True,
		unique=True,
  )
    hosp_sitesReferencia = models.CharField(
        max_length=250,
		blank=True,
		unique=True,
  )
    hosp_coresPadraoVcQuer = models.CharField(
        max_length=250,
		blank=True,
		unique=True,
  )
    hosp_coresVoceNaoQuer = models.CharField(
        max_length=250,
		blank=True,
		unique=True,
  )
    hosp_funcionalidadeExtra = models.CharField(
        max_length=250,
		blank=True,
		unique=True,
  )
    hosp_imgansFornecida = models.CharField(
        max_length=250,
		blank=True,
		unique=True,
  )
    hosp_picture = models.ImageField(
		upload_to='static/logotiposUpadate/',
		unique=True,

	)
    hosp_sobreseuwebsite = models.CharField(
        max_length=250,
		blank=True,
		unique=True,
  )
    date_created = models.DateField(
  )


#    def __repr__(self):
#        return f"Briefinghospedagem('{self.func_nameDaEmpresa}',
#                       '{self.hosp_localizacaoDaEmpresa}',
#                       '{self.hosp_EmailDaEmpresa}',
#                       '{self.hosp_conctatoDaEmpresa}',
#                       '{self.hosp_sugestaoDeDominio}',
#                       '{self.hosp_sobreSuaEmpresa}',
#                       '{self.hosp_objetivoDoSeuSite}',
#                       '{self.hosp_venderProduto}',
#                       '{self.hosp_categoriasDoSeuSite}',
#                       '{self.hosp_sitesReferencia}',
#                       '{self.hosp_coresPadraoVcQuer}',
#                       '{self.hosp_coresVoceNaoQuer}',
#                       '{self.hosp_funcionalidadeExtra}',
#                       '{self.hosp_imgansFornecida}',
#                       '{self.hosp_picture}',
#                       '{self.hosp_sobreseuwebsite}',
#                       '{self.date_created }',
#                      )"


#################################################
#
#
#
#
#################################################