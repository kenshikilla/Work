from django.test import TestCase
from .models import News

class Newstest(TestCase):
    def test_model_name(self):
        news = News.objects.create(title="bebra", content="content111")
        self.assertEqual(news.title, "bebra")

    def test_model_url(self):
        news = News.objects.create(title="bebra", content="content111")
        self.assertEqual(news.content, "content111") 
