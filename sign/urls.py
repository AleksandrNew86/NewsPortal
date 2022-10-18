

from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import UserUpdate, make_me_author

urlpatterns = [
    path('sign/logout/', LogoutView.as_view(template_name='sign/logout.html'), name='logout'),
    path('user/<int:pk>', UserUpdate.as_view(), name='user_edit'),
    path('author/', make_me_author, name='make_me_author'),
]