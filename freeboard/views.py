from django.shortcuts import render
from .models import Freeboard_Post

# Create your views here.

def index(request):
    posts = Freeboard_Post.objects.all().order_by('-pk')
    return render(
        request,
        'freeboard/index.html',
        {
            'posts' : posts,
        }
    )


def single_post_page(request, pk):
    post = Freeboard_Post.objects.get(pk=pk)

    return render(
        request,
        'freeboard/single_post_page.html',
        {
            'post' : post,
        }
    )