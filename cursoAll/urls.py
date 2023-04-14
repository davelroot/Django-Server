from django.urls import path, include
from .views import (
Online_courses,
EventsGrid,
EventsList,
Courses,
Contactos,
CursosListView,
CursosDetailView

)

app_name = 'cursosAll'

urlpatterns = [
   # path(r'^$', views.index, name='index'),
   #('', views.CursoAllView.as_view(), name='CursoAll'),
   path('online_courses', Online_courses.as_view() ,name='online_courses'),
   path("curso_list", CursosListView.as_view(), name="curso_list"),
   path("<uuid:pk>/", CursosDetailView.as_view(), name="curso_detail"),
   
   path('eventsGrid', EventsGrid ,name='eventsGrid'),
   path('eventsList', EventsList, name='eventsList'),
   path('courses', Courses ,name='courses'),
   path('contactos', Contactos ,name='contactos'),
]