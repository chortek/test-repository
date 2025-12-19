from django.db import models
from django.utils import timezone
from django.urls import reverse


class Recipe(models.Model):
    """Модель рецепта для кулинарного блога"""
    title = models.CharField(max_length=200, verbose_name="Название рецепта")
    slug = models.SlugField(max_length=200, unique=True, verbose_name="URL")
    description = models.TextField(verbose_name="Описание")
    ingredients = models.TextField(verbose_name="Ингредиенты", help_text="Каждый ингредиент с новой строки")
    instructions = models.TextField(verbose_name="Инструкция по приготовлению")
    image = models.ImageField(upload_to='recipes/', blank=True, null=True, verbose_name="Изображение")
    cooking_time = models.PositiveIntegerField(verbose_name="Время приготовления (минуты)", default=30)
    servings = models.PositiveIntegerField(verbose_name="Количество порций", default=4)
    difficulty = models.CharField(
        max_length=20,
        choices=[
            ('easy', 'Легко'),
            ('medium', 'Средне'),
            ('hard', 'Сложно'),
        ],
        default='medium',
        verbose_name="Сложность"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    published = models.BooleanField(default=True, verbose_name="Опубликовано")

    class Meta:
        verbose_name = "Рецепт"
        verbose_name_plural = "Рецепты"
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:recipe_detail', kwargs={'slug': self.slug})

    def get_ingredients_list(self):
        """Возвращает список ингредиентов"""
        return [ingredient.strip() for ingredient in self.ingredients.split('\n') if ingredient.strip()]

