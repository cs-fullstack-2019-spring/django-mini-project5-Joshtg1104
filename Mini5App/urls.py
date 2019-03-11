from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('newUser/', views.newUser, name='newUser'),
    path('addRecipe/', views.addRecipe, name='addRecipe'),
    path('details/', views.details, name='details'),
    path('edit/<int:ID>/', views.editRecipe, name='edit'),
    path('delete/<int:ID>/', views.deleteRecipe, name='delete'),
]
