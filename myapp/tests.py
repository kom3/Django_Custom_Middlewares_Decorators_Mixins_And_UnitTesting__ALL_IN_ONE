from django.test import TestCase, TransactionTestCase, SimpleTestCase
from rest_framework.test import APIRequestFactory
from .models import MyAnotherModel, MyUserModel
from .views import PostViewSet

# Create your tests here.


class TestPostViewSet(TestCase):
    databases = "__all__"

    def setUp(self):
        self.factory = APIRequestFactory()
        self.post_data = MyUserModel.objects.using(
            'mysql').get_or_create(name='Leo', age=32)

    def test_get(slef):
        view = PostViewSet.as_view({'get': 'list'})
        request = slef.factory.get("/users", pk=1)
        response = view(request)
        slef.assertEqual(response.status_code, 200)

    def test_dummy(self):
        """dummy testcase"""
        self.assertEqual('The lion says "roar"', 'The lion says "roar"')
        # self.assertEqual('The lion says "roar"', 'The cat says "meow"')
