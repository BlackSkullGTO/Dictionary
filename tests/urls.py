from django.urls import path
from . import views

urlpatterns = [
    path('', views.init_test, name='init-test'),
]