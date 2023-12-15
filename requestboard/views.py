from django.shortcuts import render
from .models import SongRequest_Post
from requestboard.forms import Form
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    posts = SongRequest_Post.objects.all().order_by('-pk')
    paginator = Paginator(posts, 7)
    page_number = request.GET.get("page")
    page_object = paginator.get_page(page_number)

    return render(
        request,
        'requestboard/index.html',
        {
            'page_object' : page_object,
            'paginator' : paginator
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
