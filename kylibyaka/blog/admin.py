from django.contrib import admin
from .models import Recipe


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'difficulty', 'cooking_time', 'servings', 'published', 'created_at')
    list_filter = ('published', 'difficulty', 'created_at')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Основная информация', {
            'fields': ('title', 'slug', 'description', 'image')
        }),
        ('Детали рецепта', {
            'fields': ('ingredients', 'instructions', 'cooking_time', 'servings', 'difficulty')
        }),
        ('Публикация', {
            'fields': ('published', 'created_at', 'updated_at')
        }),
    )


