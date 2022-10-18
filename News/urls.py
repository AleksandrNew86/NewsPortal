from django.urls import path
from .views import NewsList, NewsDetail, NewsSearch,\
    NewsCreate, NewsEdit, NewsDelete, ArticleCreate, TimeZones
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('news/', cache_page(60)(NewsList.as_view()), name='news_list'),
    path('news/<int:pk>', NewsDetail.as_view(), name='news_details'),
    path('news/search/', NewsSearch.as_view(), name='news_search'),
    path('news/create/', NewsCreate.as_view(), name='news_create'),
    path('article/create/', ArticleCreate.as_view(), name='article_create'),
    path('news/<int:pk>/edit/', NewsEdit.as_view(), name='news_edit'),
    path('news/<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
    path('timezones/', TimeZones.as_view(), name='timezones'),
]
