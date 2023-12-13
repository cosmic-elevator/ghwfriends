from django.shortcuts import render
from .models import SongRequest_Post
from requestboard.forms import Form
from django.http import HttpResponseRedirect

# Create your views here.

def index(request):
    posts = SongRequest_Post.objects.all().order_by('-pk')
    return render(
        request,
        'requestboard/index.html',
        {
            'posts' : posts,
        }
    )


def single_post_page(request, pk):
    post = SongRequest_Post.objects.get(pk=pk)

    return render(
        request,
        'requestboard/single_post_page.html',
        {
            'post' : post,
        }
    )


def write(request):
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/requestboard')
               
    else:
        form = Form()

    return render(
        request,
        'requestboard/write.html',
        {
            'form' : form
        }
    )
