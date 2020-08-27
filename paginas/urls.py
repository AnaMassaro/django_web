from django.urls import path
from . import views
from paginas.services import vendas
from django.conf.urls import url


urlpatterns = [
    path('', views.index, name='index'),
    path('cliente/', views.cliente, name='cliente'),
    path('produto/', views.produto, name='produto'),
    path('nota/', views.nota, name='nota'),
    path('listaproduto/', views.lista, name='listaproduto'),
    path('rota/', views.rota, name='rota'),
    path('listanota/', views.listanota, name='listanota'),
    path('finalizar/', views.updatenote, name='finalizar'),
    # path('vendas/', views.vendas, name='vendas'),

]