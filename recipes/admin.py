from django.contrib import admin
from recipes.models import Recipe, Tag


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    save_on_top = True
    exclude = ('slug',)
    search_fields = ['title']
    filter_horizontal = ('tags', 'related_recipes',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    save_on_top = True
    exclude = ('slug',)
