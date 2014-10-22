""" Tests for top-level USAID MMC views that aren't tested elsewhere. """

from django.contrib.auth import get_user_model
from tastypie.test import ResourceTestCase
from tastypie.models import ApiKey


class SubscriptionViewTests(ResourceTestCase):

    def setUp(self):
        super(SubscriptionViewTests, self).setUp()
        self.user = get_user_model().objects.create_user(
            username='test', email='test@example.com', password='test_pw')
        self.api_key = ApiKey.objects.create(user=self.user)

    def test_top_level(self):
        auth = self.create_apikey(self.user.username, self.api_key.key)
        response = self.api_client.get(
            '/subscription/api/v1/subscription/subscription/',
            format='json', authentication=auth)
        self.assertEqual(response.status_code, 200)
        data = self.deserialize(response)
        self.assertEqual(data['objects'], [])
        self.assertEqual(data['meta']['total_count'], 0)
