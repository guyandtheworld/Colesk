from django.test import TestCase	

class ViewTest(TestCase):
	#fixtures = ['core_views_testdata.json']
	def test_main_page(self):
		resp = self.client.get('/')
		self.assertEqual(resp.status_code, 200)
		self.assertTrue('posts' in resp.context)