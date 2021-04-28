from rest_framework import serializers
from .models import Questions, Choice, Answers
class ChoiceSerializer(serializers.ModelSerializer):
    percent = serializers.SerializerMethodField()
    class Meta:
        model = Choice
        fields = ['pk', 'title', 'points', 'percent', 'lock_other']
    def get_percent(self, obj):
        total = Answers.objects.filter(question = obj.question).count()
        current = Answers.objects.filter(question = obj.question, choice = obj).count()
        if total != 0:
            return current * 100 / total
        else:
            return 0.0
class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, source='choice_set', )
    class Meta:
        model = Questions
        fields = ['pk', 'title', 'choices', 'max_points']

class AnswerSerializer(serializers.Serializer):
    answers = serializers.JSONField()
    def validate_answers(self, answers):
        if not answers:
            raise serializers.ValidationError('Неверный ответ!')
        return answers
    def save(self):
        answers = self.data['answers']
        user = self.context.user
        for question_id in answers:
            question = Questions.objects.get(pk = question_id)
            choices=answers[question_id]
            for choice_id in choices:
                choice = Choice.objects.get(pk = choice_id)
                Answers(user = user, question = question, choice = choice).save()
                user.is_ancwer = True
                user.save()
