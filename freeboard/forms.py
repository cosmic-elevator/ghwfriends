from django.forms import ModelForm
from freeboard.models import *

class Form(ModelForm):
    class Meta:
        model = Freeboard_Post
        fields = ['title', 'author', 'content']
        #author 추가해야 함... 