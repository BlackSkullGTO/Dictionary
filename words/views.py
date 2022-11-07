# from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import Word
from .forms import WordCreateForm, WordUpdateForm

class Register(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register-success')

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.success_url)


class WordCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    template_name = 'words/word_create.html'
    form_class = WordCreateForm
    success_url = reverse_lazy('show-words')

    def form_valid(self, form):
        word = form.save(commit=False)
        try:
            word.user = self.request.user
        except Exception:
            pass
        word.save()
        return HttpResponseRedirect(self.success_url)

class WordList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    # model = Word
    context_object_name = 'all_words'

    def get_queryset(self):
        return Word.objects.filter(user=self.request.user)

class WordView(LoginRequiredMixin, DetailView):
    login_url = reverse_lazy('login')
    # model = Word
    context_object_name = 'word'

    def get_queryset(self):
        return Word.objects.filter(user=self.request.user)

class WordEdit(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    # model = Word
    template_name = 'words/word_update.html'
    context_object_name = 'word'
    form_class = WordUpdateForm
    success_url = ('show-words')

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.success_url)

class WordDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    # model = Word
    context_object_name = 'word'
    success_url = '/word/show'

    def get_queryset(self):
        return Word.objects.filter(user=self.request.user)