from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register("career-categories", views.CareerCategoryViewSet, "career-category")
router.register("questions", views.QuestionViewSet, "question")
router.register("answers", views.AnswerViewSet, "answer")
router.register("users", views.UserViewSet, 'user')
router.register("surveys", views.SurveyViewSet, 'survey')

urlpatterns = [
    path('', include(router.urls)),
    path('oauth2-info/', views.AuthInfo.as_view())
]