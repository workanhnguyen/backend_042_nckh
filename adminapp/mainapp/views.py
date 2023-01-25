from rest_framework.response import Response
from rest_framework import viewsets, generics, status, permissions
from rest_framework.decorators import action
from django.http import Http404
from rest_framework.views import APIView
from django.shortcuts import render
from rest_framework import viewsets, generics

from .models import CareerCategory, Question, Answer
from .serializers import CareerCategorySerializer, QuestionSerializer, AnswerSerializer


# Create your views here.

class CareerCategoryViewSet(viewsets.ViewSet,
                            generics.ListAPIView):
    queryset = CareerCategory.objects.all()
    serializer_class = CareerCategorySerializer

    @action(methods=['get'], detail=True, url_path='answers')
    def get_answers(self, request, pk):
        answers = CareerCategory.objects.get(pk=pk).answers

        return Response(AnswerSerializer(answers, many=True).data,
                        status=status.HTTP_200_OK)


class QuestionViewSet(viewsets.ViewSet,
                      generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    @action(methods=['get'], detail=True, url_path='answers')
    def get_answers(self, request, pk):
        answers = Question.objects.get(pk=pk).answers

        return Response(AnswerSerializer(answers, many=True).data,
                        status=status.HTTP_200_OK)


class AnswerViewSet(viewsets.ViewSet,
                    generics.ListAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
