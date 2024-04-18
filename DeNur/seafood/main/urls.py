
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.raka, name='contact'),
    path('korrrzin', views.korzin, name='korzin'),
    path('tovar', views.tovar, name='tovar')
]