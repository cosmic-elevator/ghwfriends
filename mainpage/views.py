from django.shortcuts import render
from freeboard.models import Freeboard_Post
from requestboard.models import SongRequest_Post

# Create your views here.


def index(request):
    freeboard_all_posts = Freeboard_Post.objects.all()
    requestboard_all_posts = SongRequest_Post.objects.all()
    freeboard_recent_five_posts = freeboard_all_posts[freeboard_all_posts.count()-5:] if freeboard_all_posts.count() >= 5 else freeboard_all_posts
    requestboard_recent_five_posts = requestboard_all_posts[requestboard_all_posts.count()-5:] if requestboard_all_posts.count() >= 5 else requestboard_all_posts
    return render(
        request,
        'mainpage/index.html',
        {
            'freeboard_recent_five_posts' : freeboard_recent_five_posts,
            'requestboard_recent_five_posts' : requestboard_recent_five_posts
        }
    )