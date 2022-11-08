import random
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from .forms import CreateTestForm
from words.models import Word

# В темплейте создаем поле с количеством слов в тесте и кнопку. Это будет мини форма. Если не указано количество слов, то вывести ошибку. После нажатия на кнопку, во вьюхе запускается метод генерации слов. Они добавляются в контекст и передаются во вьюху теста.
@login_required(login_url=reverse_lazy('login'))
def init_test(request):
    error = ''
    if request.method == 'POST':
        form = CreateTestForm(request.POST)
        if form.is_valid():
            word_list = generate_word_list(form.cleaned_data['word_count'], request)
            if word_list:
                print(word_list)
                return HttpResponseRedirect(reverse_lazy('show-words'))
            else:
                error = 'Ваш словарь пуст'
    else:
        form = CreateTestForm()

    return render(request, 'tests/init_test.html', {
        'form': form,
        'error': error,
    })

def generate_word_list(num, request):
    word_list = list(Word.objects.filter(user=request.user).values())
    if not word_list:
        return []
    if len(word_list) < num:
        num = len(word_list)

    word_list = random.sample(word_list, num)
    word_list = [{'id': word['id'], 'translate': word['translate']} for word in word_list]
    return word_list

# Если были переданы параметры теста (набор слов и тд), то происходит генерация темплейта страницы. Она состоит из блоков, которые в свою очередь состоят из слова и радио боксов. В конце кнопка. После нажатия происходит переход на страницу результатов. В контекст передается тот же список слов, но ещё с ответами. Также обновляются поля числа угаданности.
def test():
    pass

# Просто сверяются ответы с правильными, если есть.
def test_result():
    pass

# Пример!!
# @login_required(login_url=reverse_lazy('login'))
# def quote_req(request):
#     submitted = False
#     if request.method == 'POST':
#         form = QuoteForm(request.POST, request.FILES)
#         if form.is_valid():
#             quote = form.save(commit=False)
#             try:
#                 quote.username = request.user
#             except Exception:
#                 pass
#             quote.save()
#             return HttpResponseRedirect('/quote/?submitted=True')
#     else:
#         form = QuoteForm()
#         if 'submitted' in request.GET:
#             submitted = True

#     return render(request, 'quotes/quote.html', {
#         'form': form,
#         'page_list': Page.objects.all(),
#         'submitted': submitted})