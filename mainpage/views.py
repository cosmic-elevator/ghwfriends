from django.shortcuts import render
from freeboard.models import Freeboard_Post
from requestboard.models import SongRequest_Post

# Create your views here.


def index(request):
    freeboard_posts = Freeboard_Post.objects.all()
    requestboard_posts = SongRequest_Post.objects.all()
    return render(
        request,
        'mainpage/index.html',
        {
            'freeboard_posts' : freeboard_posts,
            'requestboard_posts' : requestboard_posts
        }
    )