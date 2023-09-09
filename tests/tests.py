from django.test import TestCase

class ViewsCanRenderTest(TestCase):

    def test_can_render_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
