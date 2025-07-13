from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, CreateView, DeleteView

from notes.forms import NoteCreateForm
from notes.models import Note
from django.utils.translation import gettext as _, activate



class NoteListView(LoginRequiredMixin, ListView):
    model = Note
    template_name = 'index.html'
    login_url = 'login/'
    extra_context = {'create_form': NoteCreateForm()}
    paginate_by = 5

class Login(LoginView):
    next_page = '/'
    template_name = 'login.html'



class Register(CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'
    success_url = '/'


class Logout(LoginRequiredMixin, LogoutView):
    next_page = '/'
    login_url = 'login/'


class NoteCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    login_url = 'login/'
    http_method_names = ['post']
    form_class = NoteCreateForm
    success_url = '/'
    success_message = _('Note created successfully!')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



class NoteDeleteView(LoginRequiredMixin, DeleteView):
    model = Note
    success_url = '/'