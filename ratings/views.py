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

class CreateRating(APIView):
    def post(self, request, *args, **kwargs):
        serializer = RatingSerializer(data=request.data)
        if serializer.is_valid():
            post_id = request.data.get('post')
            post = Post.objects.get(pk=post_id)
            serializer.save(owner=request.user, post=post)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)