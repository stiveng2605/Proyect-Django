from django.shortcuts import render, redirect
from .models import Rating
from .forms import RatingForm
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy

class RatingListView(ListView):
    model = Rating
    template_name = 'rating/rating_list.html'
    context_object_name = 'ratings'

class RatingCreateView(CreateView):
    model = Rating
    form_class = RatingForm
    template_name = 'rating/rating_form.html'
    success_url = reverse_lazy('rating_list')

# Create your views here.
