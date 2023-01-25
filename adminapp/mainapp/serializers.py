from rest_framework.serializers import ModelSerializer

from .models import CareerCategory, Question, Answer


class CareerCategorySerializer(ModelSerializer):
    class Meta:
        model = CareerCategory
        fields = "__all__"


class QuestionSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"


class AnswerSerializer(ModelSerializer):
    class Meta:
        model = Answer
        fields = "__all__"
