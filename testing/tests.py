from faker import Faker
from django.test import TestCase
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
