from django.shortcuts import render

# В темплейте создаем поле с количеством слов в тесте и кнопку. Это будет мини форма. Если не указано количество слов, то вывести ошибку. После нажатия на кнопку, во вьюхе запускается метод генерации слов. Они добавляются в контекст и передаются во вьюху теста.
def init_test(request):
    pass

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