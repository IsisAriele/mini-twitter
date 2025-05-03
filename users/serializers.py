from rest_framework import serializers
from users.models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'name', 'password', 'profile_picture', 'bio']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser(
            name=validated_data['name'],
            email=validated_data['email'],
            username=validated_data['username'],
            profile_picture=validated_data.get('profile_picture'),
            bio=validated_data.get('bio')
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
