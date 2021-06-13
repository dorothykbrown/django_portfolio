from django.shortcuts import render, get_object_or_404
from .models import Post
# Create your views here.


def all_blogs(request):
    posts = list(Post.objects.order_by('-date')[:5])
    length = len(posts)
    return render(request, 'blog/all_blogs.html', {'posts': posts, 'length': length})


def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/detail.html', {'id': post_id, 'post': post})
