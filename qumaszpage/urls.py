from django.urls import path

from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('', views.uslugi, name='uslugi'),
    path('', views.kontakt, name='kontakt'),
    path('', views.onas, name='onas'),
    path('', views.opinie, name='opinie'),
    path('', views.cennik, name='cennik'),
    path('', views.conowego, name='conowego'),
]