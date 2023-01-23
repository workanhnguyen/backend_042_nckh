from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register("career-categories", views.CareerCategoryViewSet, "career-category")

urlpatterns = [
    path('', include(router.urls))
]