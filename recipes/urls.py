from django.urls import path
from recipes.views import MainView, RecipeView

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('<slug>/', RecipeView.as_view(), name='detail'),
]
