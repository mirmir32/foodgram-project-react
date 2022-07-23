from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import (AddAndDeleteSubscribe, AddDeleteFavoriteRecipe,
                       AddDeleteShoppingCart, AuthToken, DownloadShoppingCart,
                       IngredientsViewSet, RecipesViewSet, TagsViewSet,
                       UsersViewSet, set_password)

app_name = 'api'

# С v1 не по докам будет + может заруинить фронт, насколько я понял
# По поводу фронта могу ошибаться :)

router = DefaultRouter()
router.register('users', UsersViewSet, basename='users')
router.register('tags', TagsViewSet, basename='tags')
router.register('ingredients', IngredientsViewSet, basename='ingredients')
router.register('recipes', RecipesViewSet, basename='recipes')


urlpatterns = [
     path(
          'auth/token/login/',
          AuthToken.as_view(),
          name='login'),
     path(
          'users/set_password/',
          set_password,
          name='set_password'),
     path(
          'users/<int:user_id>/subscribe/',
          AddAndDeleteSubscribe.as_view(),
          name='subscribe'),
     path(
          'recipes/<int:recipe_id>/favorite/',
          AddDeleteFavoriteRecipe.as_view(),
          name='favorite_recipe'),
     path(
          'recipes/<int:recipe_id>/shopping_cart/',
          AddDeleteShoppingCart.as_view(),
          name='shopping_cart'),
     path('recipes/download_shopping_cart/',
          DownloadShoppingCart.as_view({'get': 'download'}),
          name='download'),
     path('', include(router.urls)),
     path('', include('djoser.urls')),
     path('auth/', include('djoser.urls.authtoken')),
]
