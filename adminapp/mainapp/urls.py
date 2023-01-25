from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register("career-categories", views.CareerCategoryViewSet, "career-category")
router.register("questions", views.QuestionViewSet, "question")
router.register("answers", views.AnswerViewSet, "answer")

urlpatterns = [
    path('', include(router.urls))
]