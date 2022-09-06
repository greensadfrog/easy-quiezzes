from django.shortcuts import render

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Quiz, Question
from .serializers import QuizSerializer, RandomQuestionSerializer, QuizQuestionsSerializer


class QuizListView(generics.ListAPIView):
    serializer_class = QuizSerializer
    queryset = Quiz.objects.all()


class QuizQuestions(APIView):
    def get(self, request, format=None, **kwargs):
        quiz = Question.objects.filter(quiz__title=kwargs['topic'])
        serializer = QuizQuestionsSerializer(quiz, many=True)
        return Response(serializer.data)


class RandomQuestion(APIView):
    def get(self, request, format=None, **kwargs):
        question = Question.objects.filter(quiz__title=kwargs['topic']).order_by('?')[:kwargs['amount']]
        serializer = RandomQuestionSerializer(question, many=True)
        return Response(serializer.data)
