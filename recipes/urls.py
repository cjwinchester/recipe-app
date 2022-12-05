from django.urls import path
from recipes.views import RecipeListView, RecipeView, TagView

urlpatterns = [
    path('categories/<slug>/', TagView.as_view(), name='tag_detail'),
    path('<slug>/', RecipeView.as_view(), name='recipe_detail'),
    path('', RecipeListView.as_view(), name='recipe_list'),
]
