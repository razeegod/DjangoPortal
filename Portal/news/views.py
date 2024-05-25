from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .filters import NewsFilter
from .forms import PostForm
from .models import Post

class NewsList(ListView):
    model = Post
    ordering = 'time_in'
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 10

    def get_queryset(self):
        return Post.objects.filter(_type='N')


class NewsSearch(ListView):
    model = Post
    template_name = 'search.html'
    context_object_name = 'news_search'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = NewsFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["time_now"] = datetime.now()
        context["filterset"] = self.filterset
        return context



class NewDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'
    pk_url_kwarg = 'id'


class NewCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('News.add_post')
    form_class = PostForm
    model = Post
    template_name = 'create.html'
    context_object_name = 'create_new'

    def form_valid(self, form):
        new = form.save(commit=False)
        new._type = 'N'
        return super().form_valid(form)


class NewEdit(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    permission_required = ('News.change_post')
    model = Post
    form_class = PostForm
    template_name = 'create.html'
    pk_url_kwarg = 'id'


class NewDelete(DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = reverse_lazy('news')
    pk_url_kwarg = 'id'



class ArticlesList(ListView):
    model = Post
    ordering = 'time_in'
    template_name = 'articles.html'
    context_object_name = 'articles'
    paginate_by = 10

    def get_queryset(self):
        return Post.objects.filter(_type='A')

class ArticleCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('News.add_post')
    form_class = PostForm
    model = Post
    template_name = 'create.html'
    context_object_name = 'create_new'

    def form_valid(self, form):
        new = form.save(commit=False)
        new._type = 'A'
        return super().form_valid(form)


def print_cookies(request):
    print(request.COOKIES, request.headers.get('User-Agent'), request.session, request.user)
    return render(request, 'flatpages/default.html', )
