#from django.shortcuts import render
from rest_framework import generics
from .serializers import BucketListSerializer
from .models import BucketList

# Create your views here.

class CreateView(generics.ListCreateAPIView):
    """This class define the create behavior of our rest api"""
    queryset = BucketList.objects.all()
    serializer_class = BucketListSerializer


    def perform_create(self, serializer):
        """Save the post date when creating a new bucketlist."""
        serializer.save()

class DetailView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    queryset = BucketList.objects.all()
    serializer_class = BucketListSerializer