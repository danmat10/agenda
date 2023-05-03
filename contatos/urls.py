from django.urls import path
from . import views

urlpatterns = [
    path('', views.redirect, name='redirect'),
    path('contatos', views.index, name='home'),
    path('contatos/editar/<int:contato_id>', views.editar_contatos, name='editar_contatos'),

]
