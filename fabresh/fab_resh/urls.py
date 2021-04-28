from django.urls import path
from .views import GetQuestion, QuestionsAnswers


urlpatterns = [
    path('', GetQuestion.as_view(), name = 'base'),
    path('answer/', QuestionsAnswers.as_view())
]