from recipes.models import Recipe

from bakery.views import BuildableDetailView, BuildableListView


class MainView(BuildableListView):
    model = Recipe
    context_object_name = 'recipes'


class RecipeView(BuildableDetailView):
    model = Recipe
    context_object_name = 'recipe'
