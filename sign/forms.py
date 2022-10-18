from django.contrib.auth.models import User
from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group
from django import forms
from django.utils.translation import gettext_lazy as _


class CommonSignupForm(SignupForm):
    def save(self, request):
        user = super(CommonSignupForm, self).save(request)
        common_group = Group.objects.get(name="common")
        common_group.user_set.add(user)
        return user


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = [_('username'), _('email'), _('first_name'), _('last_name')]
        help_texts = {
            'password': '',
            'username': '',
        }
