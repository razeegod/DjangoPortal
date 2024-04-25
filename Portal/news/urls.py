from django.urls import path
from .views import NewsList, NewDetail, NewsSearch, NewCreate, NewEdit, NewDelete

urlpatterns = [
    path('', NewsList.as_view(), name='news'),
    path('<int:id>', NewDetail.as_view(), name='new'),
    path('search/', NewsSearch.as_view(), name='news_search'),
    path('create/', NewCreate.as_view(), name='new_create'),
    path('<int:id>/edit/', NewEdit.as_view(), name='new_edit'),
    path('<int:id>/delete/', NewDelete.as_view(), name='new_delete'),
]