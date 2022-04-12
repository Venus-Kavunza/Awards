from rest_framework import serializers
from .models import UserProfile, Posts, Ratings

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ['id','title', 'photo','description', 'url', 'technologies_used', 'upload_date', 'user']

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id','name', 'profile_picture', 'bio', 'phone_number']


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ratings
        fields = ['id','user', 'post', 'rating']