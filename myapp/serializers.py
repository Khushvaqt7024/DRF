from rest_framework import serializers
from .models import User


def validate_username(value):
    if 'admin' in value.lower():
        raise serializers.ValidationError("Username 'admin' bo'lishi mumkin emas.")
    return value


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    age = serializers.IntegerField(min_value=0)
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = User
        fields = '__all__'

    def validate(self, data):
        if data['first_name'] == data['last_name']:
            raise serializers.ValidationError("Ism va familiya bir xil bo'lmasligi kerak.")
        return data
