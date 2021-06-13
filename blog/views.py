from django.shortcuts import render
from .models import Post
# Create your views here.


def all_blogs(request):
    posts = list(Post.objects.order_by('-date')[:5])
    length = len(posts)
    return render(request, 'blog/all_blogs.html', {'posts': posts, 'length': length})
