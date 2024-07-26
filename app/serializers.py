from .models import User, Courses, Lessons, Videos, Coments, Likes

from rest_framework import serializers


from django_filters import rest_framework as filters


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    
class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = '__all__'


class LessonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lessons
        fields = '__all__'


class VideosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Videos
        fields = '__all__'


class ComentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coments
        fields = '__all__'


class EmailSerializer(serializers.Serializer):
    subject = serializers.CharField(max_length = 255)
    message = serializers.CharField()


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Likes
        fields = '__all__'