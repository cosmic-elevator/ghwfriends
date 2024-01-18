from django.forms import ModelForm
from requestboard.models import *

class Form(ModelForm):
    class Meta:
        model = SongRequest_Post
        fields = ['title', 'author', 'content']
        #author 추가해야 함... 