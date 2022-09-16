from django.urls import path
from .views import QuizListView, RandomQuestion, QuizQuestions

app_name = 'quiz'

urlpatterns = [
    path('', QuizListView.as_view(), name='quiz'),
    path('<str:topic>/random/<int:amount>/<int:start>/<int:end>', RandomQuestion.as_view(), name='random'),
    path('<str:topic>/questions/<int:start>/<int:end>', QuizQuestions.as_view(), name='questions'),
]