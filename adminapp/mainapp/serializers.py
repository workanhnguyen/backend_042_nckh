from rest_framework.serializers import ModelSerializer

from .models import CareerCategory, Question, Answer, User, Survey


class SurveySerializer(ModelSerializer):
    class Meta:
        model = Survey
        fields = ["id", "result", "participant"]


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "username", "password", "email", "day_of_birth", "avatar"]

        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(user.password)  # Hash code password
        user.save()

        return user


class CareerCategorySerializer(ModelSerializer):
    class Meta:
        model = CareerCategory
        fields = "__all__"


class AnswerSerializer(ModelSerializer):
    class Meta:
        model = Answer
        fields = "__all__"


class QuestionSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"

