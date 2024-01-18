from django.test import TestCase, Client
from bs4 import BeautifulSoup
from .models import Freeboard_Post

# Create your tests here.


for i in range(1, 17):
    Freeboard_Post.objects.create(
        title=str(i)+'번째 테스트 포스트입니다.',
        author='최수지',
        contents='테스트를 위한 포스트입니다. 이 포스트는 '+str(i)+'번째입니다. '
    )