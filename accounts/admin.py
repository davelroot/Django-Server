from django.contrib import admin
from .models import User, UserLibrary
#from django.contrib.auth import get_user_model
#from django.contrib.auth.admin import UserAdmin
#from .forms import CustomUserCreationForm, CustomUserChangeForm

admin.site.register(User)
admin.site.register(UserLibrary)



