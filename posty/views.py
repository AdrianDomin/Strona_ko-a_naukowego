from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.


def post_list(request):
    object_list = Post.published.all()

    return render(request,'posty/post/list.html',{'page': page,'posts': posts})




def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, status='published', publish__year=year, publish__month=month, publish__day=day)

    return render(request, 'posty/post/detail.html', {'post': post})
