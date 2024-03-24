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
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializer.ValidationError({
                'detail': 'possible duplicate'
            })
