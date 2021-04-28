from rest_framework.response import Response
from .models import Questions
from rest_framework.generics import GenericAPIView
from .serializers import QuestionSerializer, AnswerSerializer
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render


# Create your views here.
class GetQuestion(GenericAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = QuestionSerializer
    queryset = Questions.objects.all()
    def get(self, request, format = None):
        questions = Questions.objects.filter(visible = True)
        last_point = QuestionSerializer(questions, many= True)
        return Response(last_point.data)
        # print(last_point.data)
        context = {
            'items': last_point.data,
        }
        return  render('base.html', context)
class QuestionsAnswers(GenericAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = AnswerSerializer
    def post(self, request, format = None):
        answer = AnswerSerializer(data = request.data, context= request)
        if answer.is_valid(raise_exception= True):
            answer.save()
            return Response({'result': 'OK'})
