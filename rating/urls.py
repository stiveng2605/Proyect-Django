from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.RatingListView.as_view(), name='rating_list'),
    path('createRating/', views.RatingCreateView.as_view(), name='rating_create')
]

