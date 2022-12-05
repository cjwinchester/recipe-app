from recipes.models import Recipe, Tag

from bakery.views import BuildableDetailView, BuildableListView


class RecipeListView(BuildableListView):
    model = Recipe
    context_object_name = 'recipes'


class RecipeView(BuildableDetailView):
    model = Recipe
    context_object_name = 'recipe'


class TagView(BuildableDetailView):
    model = Tag
    context_object_name = 'tag'
