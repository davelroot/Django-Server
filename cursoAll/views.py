from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from .models import Cursosguardar, CarteiraMotorista

# Create your views here.
class CursoAllView(TemplateView):
    template_name = ''
    
#def Online_courses(request):

class Online_courses(TemplateView):    

    #context_object_name = "online_course"
    template_name = "onlineCourses/index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cursos'] = Cursosguardar.objects.all()
        context['cartas'] = CarteiraMotorista.objects.all()
       
        return context


class CursosListView(ListView):
    model = Cursosguardar
    context_object_name = "curso_list"
    template_name = "onlineCourses/index.html"

class CursosDetailView(DetailView):
    model = Cursosguardar
    context_object_name = "curso_detail"
    template_name = "onlineCourses/cursos_detail.html"
        
def EventsGrid(request):
    return render(request, "onlineCourses/eventsGrid.html")


def EventsList(request):
    return render("onlineCourses/eventsList.html")

def Courses(request):
    return render(request, "onlineCourses/courses.html")


def Contactos(request):
    return render(request, "onlineCourses/contacts.html")


def Aboutyou(request):
    return render(request, "onlineCourses/about.html")