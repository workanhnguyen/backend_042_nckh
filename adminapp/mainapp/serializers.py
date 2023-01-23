from rest_framework.serializers import ModelSerializer

from .models import CareerCategory


class CareerCategorySerializer(ModelSerializer):
    class Meta:
        model = CareerCategory
        fields = "__all__"
