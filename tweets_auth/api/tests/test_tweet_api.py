from django.contrib.auth.models import User
from rest_framework.test import APITestCase

from tweets.models import Tweet


class TestTweetApi(APITestCase):

    @classmethod
    def setUpClass(cls):
        super(TestTweetApi, cls).setUpClass()
        cls.user = User.objects.create_user(username='test', password='dummy')

    @classmethod
    def tearDownClass(cls):
        User.objects.all().delete()
        super(TestTweetApi, cls).tearDownClass()

    def test_adding_tweet(self):
        self.client.force_login(self.user)
        response = self.client.post('/tweets/', {
            'content': 'Test tweet'
        })
        self.assertEqual(response.status_code, 201)

        tweets = Tweet.objects.all()
        self.assertEqual(tweets.count(), 1)
        self.assertEqual(tweets[0].author, self.user)

