from django.test import TestCase
from ..models import BucketList
from ..serializers import BucketListSerializer
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse

class ViewTestCase(TestCase):
    """Test suite for the api view"""

    def setUp(self):
        """Define the test client and other test variables."""

        self.client = APIClient()
        self.bucketlist_data = {'name': 'Go to Ibiza'}
        self.response = self.client.post(
            reverse('create'),
            self.bucketlist_data,
            format="json"
        )

    def test_api_can_create_a_bucketlist(self):
        """Test the api has bucket creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_a_bucketlist(self):
        """Test the api can get a given bucketlist"""

        bucketlist = BucketList.objects.get()
        response = self.client.get(
            reverse('details',kwargs={'pk': bucketlist.id}),
            format="json")

        serializer = BucketListSerializer(bucketlist)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_api_can_update_bucketlist(self):
        """"Test the api can update a given bucketlist"""
        bucketlist = BucketList.objects.get()
        change_bucketlist = {'name': 'Jose'}
        res = self.client.put(
            reverse('details', kwargs={'pk': bucketlist.id}),
            change_bucketlist,
            format='json'
        )

        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_bucketlist(self):
        """Test the api can delete a bucketlist"""

        bucketlist = BucketList.objects.get()
        response = self.client.delete(
            reverse('details', kwargs={'pk': bucketlist.id}),
            format='json',
            follow=True
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)