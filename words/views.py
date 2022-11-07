# from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.auth.forms import UserCreationForm
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


class WordCreate(CreateView):
    template_name = 'words/word_create.html'
    form_class = WordCreateForm
    success_url = reverse_lazy('show-words')

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.success_url)

class WordList(ListView):
    model = Word
    context_object_name = 'all_words'

class WordView(DetailView):
    model = Word
    context_object_name = 'word'

class WordEdit(UpdateView):
    model = Word
    template_name = 'words/word_update.html'
    context_object_name = 'word'
    form_class = WordUpdateForm
    success_url = ('show-words')

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.success_url)

class WordDelete(DeleteView):
    model = Word
    context_object_name = 'word'
    success_url = '/word/show'