from django.contrib import admin
from .models import RecipeModel, LoginModel

# Register your models here.

admin.site.register(RecipeModel)
admin.site.register(LoginModel)
