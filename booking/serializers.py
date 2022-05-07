from rest_framework.serializers import ModelSerializer
from .models import Routes

class RoutesSerializer(ModelSerializer):
    class Meta:
        model = Routes
        fields =["starting_point","ending_point","distance"]