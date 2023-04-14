from django.contrib import admin
from .models import *
# Register your models here.


class CursosAdmin(admin.ModelAdmin):
    
    list_display = ("nomecursos", "duracaocursos", "price",)
    
admin.site.register(Cursosguardar,CursosAdmin)

admin.site.register(Formadorcurso)
admin.site.register(Periodocourso)
admin.site.register(CarteiraMotorista)                