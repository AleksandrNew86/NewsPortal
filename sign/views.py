from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.shortcuts import redirect
from .forms import  UserForm
from News.models import Category, Author


class UserUpdate(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserForm
    template_name = 'sign/user_edit.html'
    success_url = reverse_lazy("news_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_author'] = not self.request.user.groups.filter(name='authors').exists()
        context['subscribes'] = self.request.user.category_set.all()
        return context


@login_required()
def make_me_author(request):
    user = request.user
    author_group = Group.objects.get(name='authors')
    if not user.groups.filter(name='authors').exists():
        author_group.user_set.add(user)
        Author.objects.create(author=user)
        return redirect('user_edit', request.user.pk)
