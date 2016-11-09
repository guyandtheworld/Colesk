from django.test import TestCase
from .models import Post

class PostTestCase(TestCase):
	def setUp(self):
		Post.objects.create(author = 'Adarsh',title = 'This is a test', text = 'Hey im testing this, hopefully it works')

	def test_if_post_work(self):
		yo = Post.objects.get(author='Adarsh')	
		self.assertEqual(yo.author = 'Adarsh')
		self.assertEqual(yo.title = 'This is a test')