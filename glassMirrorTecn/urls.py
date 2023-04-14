from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from django.contrib import admin
from django.urls import path
from mainHome.views import MmainHomeView

urlpatterns = [
    path('admin/', admin.site.urls),

    path("accounts/", include("django.contrib.auth.urls")),
    path('', MmainHomeView.as_view(), name='index'), 
    path('', include('mainHome.urls', namespace="mainHome")),
    path('', include('markeplace.urls', namespace="markeplace")),    
    path('', include('cursoAll.urls', namespace="cursosAll")),
    path('accounts/', include('allauth.urls')),
    path('users/', include('accounts.urls', namespace="users")),

   # path('', include('glassapi.urls', namespace="webpage")),
        
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

handler403 = 'mainHome.views.error_403'
handler404 = 'mainHome.views.error_404'
handler500 = 'mainHome.views.error_500'