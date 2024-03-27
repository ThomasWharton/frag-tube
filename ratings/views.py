from rest_framework import generics, permissions
from frag_tube.permissions import IsOwnerOrReadOnly
from .models import Rating
from .serializers import RatingSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


class RatingList(generics.ListCreateAPIView):
    serializer_class = RatingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Rating.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    

class RatingDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = RatingSerializer
    queryset = Rating.objects.all()
