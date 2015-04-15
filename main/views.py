from django.shortcuts import render
from blog.models import Post
from django.views.generic import Statistics

# Create your views here.

class StatisticsView(Statistics): # представление в виде списка
    model = Post