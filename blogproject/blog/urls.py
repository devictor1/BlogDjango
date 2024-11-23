from django.urls import path
from . import views

urlpatterns = [
    path('', views.postList, name='postList'),
    path('<int:pk>/', views.postDetail, name='postDetail'),
    path('create/', views.postCreate, name='postCreate'),
    path('update/<int:pk>/', views.postUpdate, name='postUpdate'),
    path('delete/<int:pk>/', views.postDelete, name='postDelete'),
]