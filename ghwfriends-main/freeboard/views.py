from django.shortcuts import render
from .models import Freeboard_Post
from freeboard.forms import Form
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    posts = Freeboard_Post.objects.all().order_by('-pk')
    paginator = Paginator(posts, 7)
    page_number = request.GET.get("page")
    page_object = paginator.get_page(page_number)

    return render(
        request,
        'freeboard/index.html',
        {   
            'page_object' : page_object,
            'paginator' : paginator
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


def write(request):
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/freeboard')
               
    else:
        form = Form()

    return render(
        request,
        'freeboard/write.html',
        {
            'form' : form
        }
    )