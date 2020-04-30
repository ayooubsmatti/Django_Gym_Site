from django.urls import path

from . import views

urlpatterns = [
    # ex: /gimnasia/
    path('', views.index, name='index'),
    # ex: /gimnasia/5/
    path('<int:entrenador_id>/', views.detail, name='detail'),
    # ex: /gimnasia/5/results/
    path('<int:entrenador_id>/results/', views.results, name='results'),
    # ex: /gimnasia/5/vote/
    path('<int:entrenador_id>/vote/', views.vote, name='vote'),
]