from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Recipe


def recipe_list(request):
    """Список всех рецептов"""
    recipes = Recipe.objects.filter(published=True)
    
    # Пагинация
    paginator = Paginator(recipes, 6)  # 6 рецептов на страницу
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'recipes': page_obj,
        'page_obj': page_obj,
    }
    return render(request, 'blog/recipe_list.html', context)


def recipe_detail(request, slug):
    """Детальная страница рецепта"""
    recipe = get_object_or_404(Recipe, slug=slug, published=True)
    context = {
        'recipe': recipe,
    }
    return render(request, 'blog/recipe_detail.html', context)


