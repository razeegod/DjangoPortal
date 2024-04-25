import django_filters
from django import forms
from django_filters import FilterSet
from .models import Post

class NewsFilter(FilterSet):
    date = django_filters.DateFilter(widget=forms.DateInput(attrs={'type': 'date'}), field_name='time_in', lookup_expr='gt')

    class Meta:
        model = Post
        fields ={
            'heading' : ['icontains'],
            'author_id__user__username' : ['icontains'],
        }