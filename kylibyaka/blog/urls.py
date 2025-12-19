from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.recipe_list, name='recipe_list'),
    path('recipe/<slug:slug>/', views.recipe_detail, name='recipe_detail'),
]


