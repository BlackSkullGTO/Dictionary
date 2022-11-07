from django.urls import path
from .views import WordCreate, WordList, WordView, WordEdit, WordDelete

urlpatterns = [
    path('', WordCreate.as_view(), name='create-word'),
    path('show/<int:pk>/delete/', WordDelete.as_view(), name='word-delete'),
    path('show/<int:pk>/edit', WordEdit.as_view(), name='word-edit'),
    path('show/<int:pk>', WordView.as_view(), name='word-detail'),
    path('show', WordList.as_view(), name='show-words'),
]