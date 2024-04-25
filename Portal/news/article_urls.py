from django.urls import path
from .views import ArticlesList, NewDetail, NewsSearch, NewCreate, NewEdit, NewDelete, ArticleCreate

urlpatterns = [
    path('', ArticlesList.as_view(), name='articles'),
    path('<int:id>', NewDetail.as_view(), name='article'),
    path('search/', NewsSearch.as_view(), name='article_search'),
    path('create/', ArticleCreate.as_view(), name='article_create'),
    path('<int:id>/edit/', NewEdit.as_view(), name='article_edit'),
    path('<int:id>/delete/', NewDelete.as_view(), name='article_delete'),
]