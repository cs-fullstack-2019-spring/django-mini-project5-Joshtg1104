from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from .forms import RecipeModel, RecipeForm, LoginModel, LoginForm


# Create your views here.

def index(request):
    print("Index")
    if request.user.is_authenticated:
        creator = LoginModel.objects.get(username=request.user)
        allItems = RecipeModel.objects.filter(recipeForeignKey=creator)
    else:
        allItems = ""
    context = {
            "allItems": allItems
        }
    return render(request, "Mini5App/index.html", context)


def newUser(request):
    if request.method == "POST":
        print(request.POST)
        loginform = LoginForm(request.POST)
        if loginform.is_valid():
            loginform.save()
            User.objects.create_user(request.POST["username"], "", request.POST["password1"])
            return redirect('index')
        else:
            context = {
                "errors": loginform.errors,
                "form": loginform
            }
            return render(request, "Mini5App/newUser.html", context)
    else:
        loginform = LoginForm()
        context = {
            "form": loginform
        }
        return render(request, "Mini5App/newUser.html", context)


def addRecipe(request):
    recipeform = RecipeForm(request.POST or None)
    allItems = RecipeModel.objects.all()
    if request.method == "POST":
        if recipeform.is_valid():
            recipeform.save()
            return redirect('index')

    context = {
        "foodform": recipeform,
        "allItems": allItems
    }
    return render(request, "Mini5App/addRecipe.html", context)


def details(request):
    recipeform = RecipeForm(request.POST)
    creator = LoginModel.objects.get(username=request.user)
    if recipeform.is_valid():
        RecipeModel.objects.create(recipe_name=request.POST["recipe_name"], description=request.POST["description"],
                                   recipe_ingredients=request.POST["recipe_ingredients"],
                                   recipe_directions=request.POST["recipe_directions"],
                                   recipe_creator=request.POST["recipe_creator"],
                                   recipe_image=request.POST["recipe_image"], recipeForeignKey=creator)
        return redirect('index')
    else:
        context = {
            "detailform": recipeform,
            "errors": recipeform.errors
        }
        return render(request, "Mini5App/addRecipe.html", context)


def editRecipe(request, ID):
    edit = get_object_or_404(RecipeModel, pk=ID)
    if request.method == "POST":
        print("valid")
        recipeform = RecipeForm(request.POST, instance=edit)
        if recipeform.is_valid():
            recipeform.save()
        return redirect('index')
    recipeform = RecipeForm(instance=edit)
    context = {
        "editform": recipeform,
        "itemID": ID
    }
    return render(request, "Mini5App/edit.html", context)


def deleteRecipe(request, ID):
    recipeDelete = get_object_or_404(RecipeModel, pk=ID)
    recipeDelete.delete()
    return redirect('index')
