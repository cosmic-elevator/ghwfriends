from django.test import TestCase, Client
from bs4 import BeautifulSoup
from .models import Freeboard_Post

# Create your tests here.


class TestView(TestCase):
    def setup(self):
        self.client = Client()


    def test_post_list(self):
        response = self.client.get('/freeboard/')
        self.assertEqual(response.status_code, 200)

        soup = BeautifulSoup(response.content, 'html.parser')
        
        self.assertEqual(Freeboard_Post.objects.count(), 0)
        main_area = soup.find('div', id='main-area')
        self.assertIn('아직 게시물이 없습니다', main_area.text)

        post_1 = Freeboard_Post.objects.create(
            title='첫 번째 포스트입니다. ', 
            author='최수지',
            content='안녕하세요. 테스트용 포스트입니다.'
        )

        post_2 = Freeboard_Post.objects.create(
            title='두 번째 포스트입니다. ',
            author='최수지',
            content='안녕하지 않습니다. 두 번째 테스트용 포스트입니다. '
        )

        self.assertEqual(Freeboard_Post.objects.count(), 2)

        response = self.client.get('/freeboard/')
        soup = BeautifulSoup(response.content, 'html.parser')
        self.assertEqual(response.status_code, 200)

        main_area = soup.find('div', id='main-area')
        self.assertIn(post_1.title, main_area.text)
        self.assertIn(post_2.title, main_area.text)
        self.assertNotIn('아직 게시물이 없습니다', main_area.text)

