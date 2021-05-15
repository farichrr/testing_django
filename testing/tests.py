from faker import Faker
from django.test import TestCase, Client
from .models import Publisher


# Create your tests here.
fake = Faker()
class TestMyModule(TestCase):
    def setUp(self):
        self.p = Publisher(name='silent',
                           website='www.silent.com',
                           email='silent@silent.com'
                           )

    def test_create_publisher(self):
        self.assertIsInstance(self.p, Publisher)

    def test_str_representation(self):
        self.assertEquals(str(self.p), "silent")

class TestGreetingView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_greeting_view(self):
        response = self.client.get('/testing/test/')
        self.assertEquals(response.status_code, 200)