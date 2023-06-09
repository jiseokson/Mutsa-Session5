from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer

class UserModelSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'