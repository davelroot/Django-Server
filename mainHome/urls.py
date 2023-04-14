from django.urls import path, include
from .views import (MmainHomeView,
      Developerback,
      Developerfront,
      Developermobile,
      NetFlix,
      HospedagemAll,
      AssistAcessorios,
      DesigerGrafico,
      SocialMedia,
      AssistenciaTecnica,
      EventosAll,
      Softgestao,
      Jogosfull,
      Servicosnstalacaomanutecao,
      About,
      Contact,

)

app_name = 'mainHome'

urlpatterns = [
   # path(r'^$', views.index, name='index'),
   path('indexHome/', MmainHomeView.as_view(), name='indexHome'),
   path('developerback/' , Developerback, name='developerback'),
   path('developerfront/' , Developerfront, name='developerfront'),
   path('developermobile/' , Developermobile, name='developermobile'),
   path('netFlix/' , NetFlix, name='netFlix'),
   path('hospedagemAll/' , HospedagemAll, name='hospedagemAll'),
   path('AssistAcessorios/' , AssistAcessorios, name='AssistAcessorios'),
   path('desigerGrafico/' , DesigerGrafico, name='desigerGrafico'),
   path('socialMedia/' , SocialMedia, name='socialMedia'),
   path('AssistenciaTecnica/' , AssistenciaTecnica, name='AssistenciaTecnica'),
   path('eventosAll/' , EventosAll, name='eventosAll'),
   path('softgestao/' , Softgestao, name='softgestao'),
   path('jogosfull/' , Jogosfull, name='jogosfull'),
   path('servicosnstalacaomanutecao/' , Servicosnstalacaomanutecao, name='servicosnstalacaomanutecao'),
   path('about/' , About, name='about'),
   path('contact/' , Contact, name='contact'),
   
   
   

]