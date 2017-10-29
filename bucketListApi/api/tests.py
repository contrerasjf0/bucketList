from django.test import TestCase
from .models import BucketList

# Create your tests here.

class ModelTestCase(TestCase):
    """This class define the test suite for the BucketList model"""

    def setUp(self):
        """Define the teste client and other test variables."""

        self.bucketList_name = "Write world class code"
        self.bucketlist = BucketList(name = self.bucketList_name)

    def test_model_can_create_a_bucketlist(self):
        """Test the bucketlist model can create a bucketlist"""

        old_count = BucketList.objects.count()
        self.bucketlist.save()
        new_count = BucketList.objects.count()
        self.assertNotEqual(old_count, new_count)