
from django.views.generic import ListView, DetailView, CreateView,\
    UpdateView, DeleteView, View
from django.contrib.auth.mixins import PermissionRequiredMixin
from .models import Post, Category
from .filters import PostFilter
from .forms import NewsForm
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.core.cache import cache


import pytz


class TimeZones(View):
    def get(self, request):
        return render(request, 'News/timezones.html')

    def post(self, request):
        request.session['django_timezone'] = request.POST['timezone']
        return redirect('timezones')


class NewsList(ListView):
    model = Post
    ordering = '-date_creation'
    template_name = 'News/list_news.html'
    context_object_name = 'news'
    paginate_by = 10


class NewsDetail(DetailView):
    model = Post
    template_name = 'News/news.html'
    context_object_name = 'news'

    def get_object(self, *args, **kwargs):
        obj = cache.get(f'post-{self.kwargs["pk"]}', None)

        if not obj:
            obj = super().get_object(queryset=self.queryset)
            cache.set(f'post-{self.kwargs["pk"]}', obj)
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        object_post = context['object']
        categories = object_post.category_post.all()
        context['categories'] = categories
        return context

    def post(self, request, *args, **kwargs):
        if 'add_category' in request.POST:
            category_name = request.POST['add_category']
            category = Category.objects.get(name_category=category_name)
            category.subscribers.add(request.user)
        if 'delete_category' in request.POST:
            category_name = request.POST['delete_category']
            category = Category.objects.get(name_category=category_name)
            category.subscribers.remove(request.user)
        url = request.META.get('HTTP_REFERER')
        return redirect(url)


class NewsSearch(ListView):
    model = Post
    ordering = '-date_creation'
    template_name = 'News/news_search.html'
    context_object_name = 'news'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class NewsCreate(PermissionRequiredMixin, CreateView):
    form_class = NewsForm
    model = Post
    template_name = 'News/news_edit.html'
    permission_required = 'News.add_post'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.type_post = 'NW'
        return super().form_valid(form)


class ArticleCreate(PermissionRequiredMixin, CreateView):
    form_class = NewsForm
    model = Post
    template_name = 'News/article_create.html'
    permission_required = 'News.add_post'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.type_post = 'AR'
        return super().form_valid(form)


class NewsEdit(PermissionRequiredMixin, UpdateView):
    form_class = NewsForm
    model = Post
    template_name = 'News/news_edit.html'
    permission_required = 'News.change_post'


class NewsDelete(DeleteView):
    model = Post
    template_name = 'News/news_delete.html'
    success_url = reverse_lazy("news_list")
