from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.
def all_blogs(request):
    posts = Post.objects.order_by('-date')
    return render(request, 'all_blogs.html', {'posts': posts})


def detail(request, blog_id):
    post = get_object_or_404(Post, pk=blog_id)
    return render(request, 'detail.html', {'post': post})