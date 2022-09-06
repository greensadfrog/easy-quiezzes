from django.urls import path
from .views import QuizListView, RandomQuestion, QuizQuestions

app_name = 'quiz'

urlpatterns = [
    path('', QuizListView.as_view(), name='quiz'),
    path('<str:topic>/random/<int:amount>', RandomQuestion.as_view(), name='random'),
    path('<str:topic>/questions/', QuizQuestions.as_view(), name='questions'),
]