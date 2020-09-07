from app import app
from unittest import TestCase


class Test_App_Routes(TestCase):
    """Test routes for app.py"""

    def test_home_page(self):
        with app.test_client() as client:
            res = client.get('/')
            html = res.get_data(as_text=True)
            self.assertEqual(res.status_code, 200)
            self.assertIn('<h1 class="display-4">Justin Zamora</h1>', html)

    def test_contact_page(self):
        with app.test_client() as client:
            res = client.get('/contact-post')
            self.assertEqual(res.status_code, 302)
            self.assertEqual(res.location, 'http://localhost/')
