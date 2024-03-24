from django.db import IntegrityError
from rest_framework import serializers
from .models import Rating

class RatingSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Rating
        fields = [
            'id', 'owner', 'rating',
            'post', 'created_at'
        ]

    def create(self, validated_data):
        user = self.context['request'].user
        post = validated_data['post']
        
        try:
            # Check if a rating instance exists for the current user and post
            instance = Rating.objects.get(owner=user, post=post)
            instance.rating = validated_data.get('rating', instance.rating)
            instance.save()
            return instance
        except Rating.DoesNotExist:
            # Create a new rating instance
            return Rating.objects.create(owner=user, **validated_data)
