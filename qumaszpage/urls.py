from django.urls import path

from . import views

urlpatterns = [
    path(r'', views.main, name='main'),
    path(r'', views.uslugi, name='uslugi'),
    path(r'', views.kontakt, name='kontakt'),
    path(r'', views.onas, name='onas'),
    path(r'', views.opinie, name='opinie'),
    path(r'', views.cennik, name='cennik'),
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('', views.opinion_list, name='opinion_list'),
    path('opinion/new/', views.opinion_new, name='opinion_new'),
    path('opinion/<int:pk>/edit/', views.opinion_edit, name='opinion_edit'),
]