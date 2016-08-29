from django.shortcuts import render, HttpResponse
from django.views.generic import View

from .models import Post
# Create your views here.


def index(request):

    post_objects = Post.objects.all()

    return render(request, 'index.html', {'post_objects': post_objects})

