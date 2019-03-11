from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class LoginModel(models.Model):
    name = models.CharField(max_length=70, default="")
    username = models.CharField(max_length=70, default="")
    password1 = models.CharField(max_length=200, default="")
    password2 = models.CharField(max_length=200, default="")
    email_address = models.EmailField(default="")
    profile_picture = models.CharField(max_length=800, default="")
    userForeignKey = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name


class RecipeModel(models.Model):
    recipe_name = models.CharField(max_length=200, default="")
    description = models.CharField(max_length=1000, default="")
    recipe_ingredients = models.CharField(max_length=3000, default="")
    recipe_directions = models.CharField(max_length=3000, default="")
    date_created = models.DateField()
    recipe_creator = models.CharField(max_length=60, default="")
    recipe_image = models.CharField(max_length=800, default="")
    recipeForeignKey = models.ForeignKey(LoginModel, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.recipe_name
