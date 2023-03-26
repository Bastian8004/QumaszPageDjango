from django.urls import path

from . import views

urlpatterns = [
    path('', views.main),
    path('main', views.main, name="main"),
    path('uslugi', views.uslugi),
    path('kontakt', views.kontakt),
    path('onas', views.onas),
    path('cennik', views.cennik),
    path('conowego', views.post_list),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new),
    path('post/<int:pk>/edit/', views.post_edit),
    path('opinie', views.opinion_list, name='opinie'),
    path('opinion/new/', views.opinion_new),
    path('opinion/<int:pk>/edit/', views.opinion_edit),
]