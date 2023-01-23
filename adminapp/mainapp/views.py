from django.shortcuts import render
from rest_framework import viewsets, generics

from .models import CareerCategory
from .serializers import CareerCategorySerializer


# Create your views here.

class CareerCategoryViewSet(viewsets.ViewSet,
                            generics.ListAPIView):
    queryset = CareerCategory.objects.all()
    serializer_class = CareerCategorySerializer
