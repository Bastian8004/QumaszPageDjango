from django.urls import path

from . import views

urlpatterns = [
    path('main', views.main),
    path('uslugi', views.uslugi),
    path('kontakt', views.kontakt),
    path('onas', views.onas),
    path('opinie', views.opinie),
    path('cennik', views.cennik),
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('', views.opinion_list, name='opinion_list'),
    path('opinion/new/', views.opinion_new, name='opinion_new'),
    path('opinion/<int:pk>/edit/', views.opinion_edit, name='opinion_edit'),
]