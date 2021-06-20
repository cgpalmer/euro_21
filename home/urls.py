from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('add/', views.add_match, name='add_match'),
]