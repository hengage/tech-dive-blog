from django.shortcuts import get_object_or_404, render
#from django.views import generic
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse, reverse_lazy
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import UserPassesTestMixin

from .forms import CustomUserCreationForm, UpdateUserForm

User = get_user_model()
class UpdateUserView(UserPassesTestMixin, UpdateView):
    form_class = UpdateUserForm
    model = User
    context_object_name = 'current_user'
    template_name = 'user/update_user.html'

    def get_success_url(self):
        return reverse('update_user', kwargs={'pk': self.get_object().id})

    def test_func(self):
        obj = self.get_object()
        return obj == self.request.user